//Realiza un programa que reciba el siguiente objeto, e imprima otro objeto con los siguientes datos:

// Entrada

/* Y SALGA:

const result = {
	name: "John Doe",
	gradeAvg: 85.6,
	highesGrade: "science",
	lowestGrade: "history"
} 
    
*/



const student = {
    name: "John Doe",
    grades: [
      { name: "math", grade: 80 },
      { name: "science", grade: 100 },
      { name: "history", grade: 60 },
      { name: "PE", grade: 90 },
      { name: "music", grade: 98 }
    ]
  };



let total = 0;


let highest = student.grades[0];
let lowest = student.grades[0];


for (let i of student.grades) {
    total += i.grade;
    if (i.grade > highest.grade) {
        highest = i;
    }

    if (i.grade < lowest.grade) {
        lowest = i;
}}


const result = {
    name: student.name,
    gradeAvg: (total / student.grades.length).toFixed(1),
    highesGrade: highest.name,
    lowestGrade: lowest.name
};

console.log(result);
