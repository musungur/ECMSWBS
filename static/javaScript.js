
var helloworld = {
    intro: "Hello World",
    message: "Welcome to the world of javascript"
}
/*
console.log(helloworld)
document.getElementById("useroutput").innerHTML = 3*5;
print("Hello World. This is Robert")
document.write("Robert Musungu")
*/

// id=useroutput - Display-button-function
function userOutputInnHtmlDisplay(){
    const userOutput1 = document.getElementById("userInput").value;
    document.getElementById("useroutput").innerHTML = "My name is "+userOutput1+".";
}

// id=useroutput - Delete/remove-display-function
function userOutputRemoveDeleteInnHtml(){
    document.getElementById("useroutput").innerHTML = "";
}

// id=useroutput - Add/append -Function
function userOutputADDtoInnHtml(){
    const userInputs = document.getElementById("userInput").value;
    document.getElementById("useroutput").append("My name is "+userInputs+".");
}
// delay - on python button form1
function pyThonForm1Delay(){
    let typed = document.getElementById("py").value;
    document.getElementById("useroutput").innerHTML = "Submitting your inputs: '..."+ typed + "...'";
    setTimeout(function(){
        document.getElementById("useroutput").innerHTML = "Submitted successful!!";
    },3000)
}

// read from Backup - Form3 display in id=FromOutside
function GetDataRead(){
    document.getElementById("FromOutside").innerHTML = data;
}

// read date id=DateTime
function DateToday(){
    document.getElementById("DateTime").innerHTML = dateANDtime;
}
