
// function startPrinting(){
// 	change();
// 	var start = document.getElementById("start-date").value
// 	var end = document.getElementById("end-date").value
// 	eel.start_printing(start, end)
//
// }


function startPrinting()	{

	var elem = document.getElementById("mybutton1")
	var start = document.getElementById("start-date").value
	var end = document.getElementById("end-date").value
	if (elem.innerHTML=="Start AI")	{
		elem.innerHTML = "Process running!"
		eel.start_printing(start, end)
	}
	// else elem.innerHTML = "Start AI"

}





eel.expose(mainUpdate)
function mainUpdate(update)	{
	document.getElementById("update-status").innerHTML = update

}

eel.expose(statUpdate)
function statUpdate(status)	{
	document.getElementById("updatetwo").innerHTML = status

}

eel.expose(statDeetsUpdate)
function statDeetsUpdate(deets)	{
	document.getElementById("updatethree").innerHTML = deets

}

function change() {
  document.getElementById('mybutton1').innerHTML= "Process running!";
}

eel.expose(changeBack)
function changeBack() {
  document.getElementById('mybutton1').innerHTML= "Start AI";
}

eel.expose(buttonETA)
function buttonETA(buttoneta)	{
	document.getElementById('mybutton1').innerHTML= buttoneta
}
