class DuadTodoApp {
    constructor(){
      this.user = null;
      this.tasks = [];
      this.filter = 'all';
      this.init();
    }
  
    init(){

      qs('#go-register').addEventListener('click', e => { e.preventDefault(); this.swapAuth('register'); });
      qs('#go-login').addEventListener('click', e => { e.preventDefault(); this.swapAuth('login'); });
      qs('#login-form').addEventListener('submit', e => this.login(e));
      qs('#register-form').addEventListener('submit', e => this.register(e));
      qs('#logout').addEventListener('click', () => this.logout());
  

      qs('#add').addEventListener('click', () => this.add());
      qs('#new-task').addEventListener('keydown', e => { if (e.key === 'Enter') this.add(); });
  

      qsa('.tab').forEach(b => b.addEventListener('click', e => this.setFilter(e.target.dataset.filter)));
  

      const saved = localStorage.getItem('duad-current-user');
      if (saved){ this.user = saved; this.showApp(); this.load(); }
    }
  

    swapAuth(mode){
      const showLogin = mode === 'login';
      toggle(qs('#login-card'), !showLogin);
      toggle(qs('#register-card'), showLogin);
    }
  
    login(e){
      e.preventDefault();
      const u = qs('#login-username').value.trim();
      const p = qs('#login-password').value;
      const users = JSON.parse(localStorage.getItem('duad-users') || '{}');
      if (users[u] && users[u] === p){
        this.user = u;
        localStorage.setItem('duad-current-user', u);
        this.showApp();
        this.load();
      } else {
        alert('Invalid username or password');
      }
    }
  
    register(e){
      e.preventDefault();
      const u = qs('#reg-username').value.trim();
      const p = qs('#reg-password').value;
      const c = qs('#reg-confirm').value;
  
      if (p !== c) return alert('Passwords do not match');
      if (p.length < 6) return alert('Password must be at least 6 characters');
  
      const users = JSON.parse(localStorage.getItem('duad-users') || '{}');
      if (users[u]) return alert('Username already exists');
  
      users[u] = p;
      localStorage.setItem('duad-users', JSON.stringify(users));
      this.user = u;
      localStorage.setItem('duad-current-user', u);
      this.showApp();
      this.load();
    }
  
    logout(){
      localStorage.removeItem('duad-current-user');
      this.user = null;
      this.tasks = [];
      qs('#user-label').textContent = '';
      toggle(qs('#app'), true);
      toggle(qs('#auth'), false);
      qs('#login-form').reset();
      qs('#register-form').reset();
    }
  
    showApp(){
      toggle(qs('#auth'), true);
      toggle(qs('#app'), false);
      qs('#user-label').textContent = `Logged in as ${this.user}`;
    }
  

    load(){
      const raw = localStorage.getItem(`duad-tasks-${this.user}`);
      this.tasks = raw ? JSON.parse(raw) : [];
      this.render();
      this.updateStats();
    }
    save(){
      localStorage.setItem(`duad-tasks-${this.user}`, JSON.stringify(this.tasks));
    }
  

    add(){
      const input = qs('#new-task');
      const text = input.value.trim();
      if (!text) return;
      const task = { id: Date.now().toString(), text, completed:false };
      this.tasks.unshift(task);
      input.value = '';
      this.save(); this.render(); this.updateStats();
    }
  
    toggle(id){
      const t = this.tasks.find(x => x.id === id);
      if (!t) return;
      t.completed = !t.completed;
      this.save(); this.render(); this.updateStats();
    }
  
    remove(id){
      this.tasks = this.tasks.filter(x => x.id !== id);
      this.save(); this.render(); this.updateStats();
    }
  
    edit(id, text){
      const t = this.tasks.find(x => x.id === id);
      if (!t) return;
      const v = text.trim();
      if (v) t.text = v;
      this.save(); this.render();
    }
  

    setFilter(f){
      this.filter = f;
      qsa('.tab').forEach(b => b.classList.toggle('active', b.dataset.filter === f));
      this.render();
    }
  
    filtered(){
      if (this.filter === 'active') return this.tasks.filter(t => !t.completed);
      if (this.filter === 'completed') return this.tasks.filter(t => t.completed);
      return this.tasks;
    }
  
    render(){
      const list = qs('#list');
      const empty = qs('#empty');
  

      qsa('.item').forEach(el => el.remove());
  
      const data = this.filtered();
      if (!data.length){
        toggle(empty, false);
        this.updateEmpty();
        return;
      }
      toggle(empty, true);
  
      data.forEach(t => {
        const el = document.createElement('div');
        el.className = 'item';
        el.innerHTML = `
          <div class="check ${t.completed ? 'done':''}" data-id="${t.id}">${t.completed?'✓':''}</div>
          <div class="text ${t.completed ? 'done':''}" data-id="${t.id}">${escapeHtml(t.text)}</div>
          <input class="edit hidden" value="${escapeHtml(t.text)}" />
          <div class="actions">
            <button class="btn icon" data-edit>✏️</button>
            <button class="btn icon" data-del>🗑️</button>
          </div>`;
  

        el.querySelector('.check').onclick = () => this.toggle(t.id);
        el.querySelector('[data-del]').onclick = () => this.remove(t.id);
        const txt = el.querySelector('.text');
        const inp = el.querySelector('.edit');
        const start = () => { txt.classList.add('hidden'); inp.classList.remove('hidden'); inp.focus(); inp.select(); };
        const finish = () => { this.edit(t.id, inp.value); txt.classList.remove('hidden'); inp.classList.add('hidden'); };
        el.querySelector('[data-edit]').onclick = start;
        txt.ondblclick = start;
        inp.onkeydown = (e)=>{ if(e.key==='Enter') finish(); if(e.key==='Escape'){inp.value=t.txt; txt.classList.remove('hidden'); inp.classList.add('hidden');}};
        inp.onblur = finish;
  
        list.insertBefore(el, empty);
      });
    }
  
    updateEmpty(){
      const icon = qs('#empty .icon');
      const h = qs('#empty h3');
      const p = qs('#empty p');
      if (this.filter==='active'){ icon.textContent='✨'; h.textContent='No active tasks'; p.textContent='All your tasks are completed!'; }
      else if (this.filter==='completed'){ icon.textContent='🎯'; h.textContent='No completed tasks'; p.textContent='Complete some tasks to see them here.'; }
      else { icon.textContent='📝'; h.textContent='No tasks yet'; p.textContent='Add your first task to get started!'; }
    }
  
    updateStats(){
      const active = this.tasks.filter(t=>!t.completed).length;
      const done = this.tasks.length - active;
      qs('#active-count').textContent = `${active} Active`;
      qs('#done-count').textContent = `${done} Completed`;
    }
  }
  

  const qs = s => document.querySelector(s);
  const qsa = s => Array.from(document.querySelectorAll(s));
  const toggle = (el, hide) => el.classList.toggle('hidden', hide);
  const escapeHtml = s => s.replace(/[&<>"']/g, m => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m]));
  
  let app;
  document.addEventListener('DOMContentLoaded', ()=> app = new DuadTodoApp());
  