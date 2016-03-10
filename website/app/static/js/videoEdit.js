var videoA;
$(document).ready(function() {
	var count = 2;
	$('.addCat').click(function(){
		$('.weeks').find('li:last').prev().after("<li><div class='left-side'>"
			+"<a>Week "+(++count)+"</a></div><div class='right-side'>"
			+"<ul class='videos'><div class='addVid'>"
			+"<img src='staticImg/addButton.png'>"
			+"<a>Add Another Link</a></add></div></ul></li>");
	});

});

$(document).on('click', '.addVid', function(){
	videoA=$(this).parent('ul').find('.addVid');
	console.log(videoA);
	if (videoA.length==0) {
		videoA=$(this).parent('ul').find('.addVid');
	}
	$('.overlay').css('display', 'block');
	$('.get-url').css('display', 'block');
	});

$(document).on('click', '.get-url .add', function () {
	videoA.before(("<li>"+$('.get-url .name ').val()+"</li>"));
	$('.get-url input').val('');
	$('.overlay').hide();
	$('.get-url').hide();
});

$(document).on('click', '.get-url .cancel', function () {
	$('.get-url input').val('');
	$('.overlay').hide();
	$('.get-url').hide();
});