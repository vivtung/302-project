$(document).ready(function() {
	$('.list-group-item').click(function() {
		$('html, body').animate({ scrollTop: $('.list-group-item').offset().top-500}, 500);
	});
	var distanceTravel = 0;
	 $(document).mousemove(function(e){
	 	distanceTravel+=0.0000005;
	 	Math.floor(distanceTravel);
	 	$('.overlay').css('opacity', distanceTravel);
	 });
});
