function functionA(someParameter, otherParameter, callbackFunction) {
    // something with someParameter and otherParameter
    console.log(someParameter + otherParameter);
    // calls callback
    callbackFunction();
}



functionA(2, 4, () => {
    console.log("Callback executed");
});