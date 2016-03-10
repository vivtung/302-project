var videoA;
var add = null;
$(document).ready(function() {

	var count = 2;
	$('.addCat').click(function(){
		$('.weeks').find('li:last').prev().after("<li><div class='left-side'>"
			+"<a>Section "+(++count)+"</a></div><div class='right-side'>"
			+"<ul class='videos'><div class='addVid'>"
			+"<img src='../static/Img/addButton.png'>"
			+"<a>Add Another Link</a></add></div></ul></li>");
	});



	$(document).on('click', '.addVid', function(){
		videoA=$(this).parent('ul').find('.addVid');
		if (videoA.length==0) {
			videoA=$(this).parent('ul').find('.addVid');
		}
		$('.overlay').css('display', 'block');
		$('.get-url').css('display', 'block');
		$('.add').text('Add');
		$('.overlay').animate({ opacity: '0.6'}, 'slow');
		$('.get-url').animate({ opacity: '1'}, 'slow');


		});


	$(document).on('click', '.get-url .add', function () {
		if(add==null) {
			videoA.before(("<li><div class='vid' url=\" "+$('.get-url .url').val()+" \">"+$('.get-url .name ').val()+"</div></li>"));

			$('.get-url input').val('');

			
		} else {
			add.attr('url', $('.get-url .url').val());
			add.text($('.get-url .name ').val());
			$('.get-url input').val('');
			add = null;
		}
		$('.overlay').animate({ opacity: '0'}, function() {
			$('.overlay').hide();
		});
		$('.get-url').animate({ opacity: '0'}, function() {
			$('.get-url').hide();
		});
		
		
	});

	$(document).on('click', '.get-url .cancel', function () {
		$('.get-url input').val('');
		$('.overlay').animate({ opacity: '0'}, function() {
			$('.overlay').hide();
		});
		$('.get-url').animate({ opacity: '0'}, function() {
			$('.get-url').hide();
		});
		add =null;
	});

	$(document).on('click', '.vid', function() {
		$('.overlay').css('display', 'block');
		$('.get-url').css('display', 'block');
		$('.overlay').animate({ opacity: '0.6'}, 'slow');
		$('.get-url').animate({ opacity: '1'}, 'slow');
		$('.get-url .name').val($(this).text());
		$('.get-url .url').val($(this).attr('url'));

		$('.add').text('Change');
		add = $(this);
	});
});