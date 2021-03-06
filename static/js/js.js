$(document).ready(function(){

	var header = $(".blog_header");
	var content = $(".blog_content");
	var header_height = header.height();
	var treshold = header_height - 50;

	handle_scroll();

	$(document).on("scroll", function(evt){
		handle_scroll();
	});

	function handle_scroll()
	{
		pos = $(document).scrollTop();

		if(pos > treshold) { add_classes(); }
		else if (pos < treshold)
		{
			remove_classes();
			if(pos < 273) { calc_background_pos(pos); }
		}
	}

	function calc_background_pos(pos)
	{
		//back_pos = Math.sqrt( (pos - 325) );
		back_pos = pos / 10;
		console.log(back_pos);
		//if( back_pos > 1 && back_pos < 3) back_pos = back_pos / 2;
		header.css("background-position", "0 -".concat(back_pos, "%"));
	}

	function add_classes()
	{
		header.addClass("blog_header_fixed");
		content.addClass("blog_content_absolute");
	}

	function remove_classes()
	{
		header.removeClass("blog_header_fixed");
		content.removeClass("blog_content_absolute");
	}

});