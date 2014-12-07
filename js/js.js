$(document).ready(function(){

	var header = $(".blog_header");
	var content = $(".blog_content");

	$(document).on("scroll", function(evt){

		pos = $(document).scrollTop() + header.height();

		if(pos > 600)
		{
			header.addClass("blog_header_fixed");
			content.addClass("blog_content_absolute");			
		}
		else if (pos < 600)
		{
			header.removeClass("blog_header_fixed");
			content.removeClass("blog_content_absolute");
			if(pos > 300)
			{
				//back_pos = Math.sqrt( (pos - 325) );
				back_pos = (pos - 325) / 10;
				console.log();
				//if( back_pos > 1 && back_pos < 3) back_pos = back_pos / 2;
				header.css("background-position", "0 -".concat(back_pos, "%"));
			}
		}


	});

});