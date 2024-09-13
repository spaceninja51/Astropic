// Variable Examples
let variable = "variable"
document.getElementById("variableP").textContent = variable
const constant = "constant"
document.getElementById("constP").textContent = constant
// console.log(`${variable} is how you include a variable in backticks`)
// Accepting input
/* Window prompt is easiser
HTML Textbox looks/works better */
// Changes the heading to the inputted text
document.getElementById("mySubmit").onr = function(){
    input = document.getElementById("myText").value
    document.getElementById("myH1").textContent = `${input}`
}