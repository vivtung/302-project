var qcounter=2;
function nextQuestion()
{
	var qdiv = document.getElementById("qcol");
	var adiv = document.getElementById("acol");
	var counter = document.getElementById("counter");
	counter.value = qcounter;
	var qstring= "<div class=\"row\" style=\"margin-bottom:6px\">Question "+qcounter+"</div>"
		+"<div class=\"row\">"
		+"<input type=\"text\" style=\"width:40%\" name=\"q"+qcounter+"_time_min\"></input> : "
		+"<input type=\"text\" style=\"width:40%\" name=\"q"+qcounter+"_time_sec\"></input>"
		+"</div><br>";
	qdiv.innerHTML= qdiv.innerHTML+qstring;

	var astring="<div class=\"row\">"
		+"<input type=\"text\" style=\"width:100%\" name=\"q"+qcounter+"_text\"></input>"
		+"</div>"
		+"<div class=\"row\">"
		+"<input type=\"text\" style=\"width:20%\" name=\"q"+qcounter+"_ans1\"></input>"
		+"<input type=\"radio\" name=\"q"+qcounter+"_correct\" value=\"ans1\"></input>"
		+"<input type=\"text\" style=\"width:20%\" name=\"q"+qcounter+"_ans2\"></input>"
		+"<input type=\"radio\" name=\"q"+qcounter+"_correct\" value=\"ans2\"></input>"
		+"<input type=\"text\" style=\"width:20%\" name=\"q"+qcounter+"_ans3\"></input>"
		+"<input type=\"radio\" name=\"q"+qcounter+"_correct\" value=\"ans3\"></input>"
		+"<input type=\"text\" style=\"width:20%\" name=\"q"+qcounter+"_ans4\"></input>"
		+"<input type=\"radio\" name=\"q"+qcounter+"_correct\" value=\"ans4\"></input>"
		+"</div><br>";
	adiv.innerHTML= adiv.innerHTML+astring;
	qcounter++;
}
