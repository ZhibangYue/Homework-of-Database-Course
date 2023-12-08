// JavaScript Document

    /*--
		    Header Sticky
    -----------------------------------*/
    $(window).on('scroll', function(event) {    
        var scroll = $(window).scrollTop();
        if (scroll < 150) {
            $(".header-bottom, .header-mobile").removeClass("sticky");
        } else{
            $(".header-bottom, .header-mobile").addClass("sticky");
        }
    });

    /*-----------------------------------------
		Off Canvas Search
	-------------------------------------------*/

	$(".header-action-btn-search").on('click', function () {
		$("body").addClass('fix');
		$(".offcanvas-search").addClass('open');
	});

	$(".offcanvas-btn-close,.body-overlay").on('click', function () {
		$("body").removeClass('fix');
		$(".offcanvas-search").removeClass('open');
	});
	


/*--
        Off Canvas Cart
	-----------------------------------*/	
	$(".header-action-btn-cart").on('click', function () {
		$("body").addClass('fix');
		$(".cart-offcanvas-wrapper").addClass('open');
	});

	$(".offcanvas-btn-close,.offcanvas-overlay").on('click', function () {
		$("body").removeClass('fix');
		$(".cart-offcanvas-wrapper").removeClass('open');
    });



/*--
        Off Canvas Menu
	-----------------------------------*/	
	$('.mobile-menu-open').on('click', function(){
        $('.offcanvas-menu').addClass('open')
        $('.menu-overlay').addClass('open')
    });
    
    $('.menu-close').on('click', function(){
        $('.offcanvas-menu').removeClass('open')
        $('.menu-overlay').removeClass('open')
    });
    
    $('.menu-overlay').on('click', function(){
        $('.offcanvas-menu').removeClass('open')
        $('.menu-overlay').removeClass('open')
    });
	
/*--
        Product Quantity
    -----------------------------------*/
    $('.add').on('click', function () {
        if ($(this).prev().val()) {
            $(this).prev().val(+$(this).prev().val() + 1);
        }
    });
    $('.sub').on('click', function () {
        if ($(this).next().val() > 1) {
            if ($(this).next().val() > 1) $(this).next().val(+$(this).next().val() - 1);
        }
    });
	
    /*Variables*/
    var $offCanvasNav = $('.mobile-ayira-menu'),
    $offCanvasNavSubMenu = $offCanvasNav.find('.sub-menu, .mega-sub-menu, .menu-item ');

    /*Add Toggle Button With Off Canvas Sub Menu*/
    $offCanvasNavSubMenu.parent().prepend('<span class="mobile-menu-expand"></span>');

    /*Close Off Canvas Sub Menu*/
    $offCanvasNavSubMenu.slideUp();

    /*Category Sub Menu Toggle*/
    $offCanvasNav.on('click', 'li a, li .mobile-menu-expand, li .menu-title', function(e) {
        var $this = $(this);
        if (($this.parent().attr('class').match(/\b(menu-item-has-children|has-children|has-sub-menu)\b/)) && ($this.attr('href') === '#' || $this.hasClass('mobile-menu-expand'))) {
            e.preventDefault();
            if ($this.siblings('ul:visible').length) {
                $this.parent('li').removeClass('active-expand');
                $this.siblings('ul').slideUp();
            } else {
                $this.parent('li').addClass('active-expand');
                $this.closest('li').siblings('li').find('ul:visible').slideUp();
                $this.closest('li').siblings('li').removeClass('active-expand');
                $this.siblings('ul').slideDown();
            }
        }
    });

    $( ".sub-menu, .mega-sub-menu, .menu-item" ).parent( "li" ).addClass( "menu-item-has-children" );
    $( ".ayira-menu .mega-sub-menu" ).parent( "li" ).css( "position", "static" );


/*--
		Rating Script
	-----------------------------------*/

	$("#rating li").on('mouseover', function(){
		var onStar = parseInt($(this).data('value'), 10);
		var siblings = $(this).parent().children('li.star');
		Array.from(siblings, function(item){
			var value = item.dataset.value;
			var child = item.firstChild;
			if(value <= onStar){
				child.classList.add('hover')
			} else {
				child.classList.remove('hover')
			}
		})
	})

	$("#rating").on('mouseleave', function(){
		var child = $(this).find('li.star i');
		Array.from(child, function(item){
			item.classList.remove('hover');
		})
	})
	
	$('#rating li').on('click', function(e) {
		var onStar = parseInt($(this).data('value'), 10);
		var siblings = $(this).parent().children('li.star');
		Array.from(siblings, function(item){
			var value = item.dataset.value;
			var child = item.firstChild;
			if(value <= onStar){
				child.classList.remove('hover', 'fa-star-o');
				child.classList.add('fa-star')
			} else {
				child.classList.remove('fa-star');
				child.classList.add('fa-star-o')
			}
		})
    }) 



 /*--
		Checkout Payment Active
	-----------------------------------*/
	var checked = $('.payment-radio input:checked')
	if (checked) {
		$(checked).siblings('.payment-details').slideDown(500);
	};
	$('.payment-radio input').on('change', function() {
		$('.payment-details').slideUp(500);
		$(this).siblings('.payment-details').slideToggle(500);
	});
    
   

    /*--
        Data Tooltip
    -----------------------------------*/
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-tooltip="tooltip"]'))
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
       return new bootstrap.Tooltip(tooltipTriggerEl)
    })
	
   /*--
        Product Color Active
    -----------------------------------*/
    $('.color-list li').each(function() {
		var get_color = $(this).attr('data-color');
		$(this).css("background-color", get_color);
    });
    
	$('.color-list li').on("click", function() {
		$(this).siblings(this).removeClass('active').end().addClass('active');
    });
	
	
	   /*--
        Product Color Active
    -----------------------------------*/
    $('.color-list a').each(function() {
		var get_color = $(this).attr('data-color');
		$(this).css("background-color", get_color);
    });
    
	$('.color-list a').on("click", function() {
		$(this).siblings(this).removeClass('active').end().addClass('active');
    });
	
	   /*--
        widget-size
    -----------------------------------*/
	$('.widget-size li').on("click", function() {
		$(this).siblings(this).removeClass('active').end().addClass('active');
    });


    // -------------------------------------------------------------
    //  Owl Carousel New Arrivals
    // -------------------------------------------------------------

    $("#new_arrivals").owlCarousel({
        items:4,
        margin:30,
        nav:true,
        autoplay:false,
        autoplayHoverPause:true,
        loop:false,
        navText: [
         "<i class='flaticon-left-arrow'></i>",
          "<i class='flaticon-right-arrow'></i>"
        ],
        responsive: {
            0: {
                items: 1,
            },
			576: {
                items: 2,
            },
            768: {
                items: 3,
                slideBy:2
            },
            991: {
                items: 3,
                loop:true,
                 dots:true,
            },
            1000: {
                items: 4,
                loop:true,
            },
        }            

    });
	
	
    // -------------------------------------------------------------
    //  Owl Carousel New Arrivals
    // -------------------------------------------------------------
	
	
	
	    // -------------------------------------------------------------
    //  Owl Carousel Collections
    // -------------------------------------------------------------

    $("#collections").owlCarousel({
        items:4,
        margin:30,
        nav:true,
        autoplay:false,
        autoplayHoverPause:true,
        loop:false,
        navText: [
         "<i class='flaticon-left-arrow'></i>",
          "<i class='flaticon-right-arrow'></i>"
        ],
        responsive: {
            0: {
                items: 1,
            },
			576: {
                items: 2,
            },
            768: {
                items: 3,
            },
            991: {
                items: 3,
                loop:true,
                 dots:true,
            },
            1000: {
                items: 4,
                loop:true,
            },
        }            

    });
	
	
    // -------------------------------------------------------------
    //  Owl Carousel Collections
    // -------------------------------------------------------------


	    // -------------------------------------------------------------
    //  Owl Carousel lookbook
    // -------------------------------------------------------------

    $("#lookbook").owlCarousel({
        items:4,
        margin:30,
        nav:true,
        autoplay:false,
        autoplayHoverPause:true,
        loop:false,
        navText: [
         "<i class='flaticon-left-arrow'></i>",
          "<i class='flaticon-right-arrow'></i>"
        ],
        responsive: {
            0: {
                items: 1,
            },
			576: {
                items: 2,
            },
            768: {
                items: 2,
            },
            991: {
                items: 2,
                loop:true,
                 dots:true,
            },
            1000: {
                items: 2,
                loop:true,
            },
        }            

    });
	
	
    // -------------------------------------------------------------
    //  Owl Carousel lookbook
    // -------------------------------------------------------------



	    // -------------------------------------------------------------
    //  Owl Carousel Best Selling
    // -------------------------------------------------------------

    $("#best_selling").owlCarousel({
        items:4,
        margin:30,
        nav:true,
        autoplay:false,
        autoplayHoverPause:true,
        loop:false,
        navText: [
         "<i class='flaticon-left-arrow'></i>",
          "<i class='flaticon-right-arrow'></i>"
        ],
        responsive: {
            0: {
                items: 1,
                slideBy:1
            },
			576: {
                items: 2,
            },
            768: {
                items: 3,
                slideBy:3
            },
            991: {
                items: 3,
                loop:true,
                 dots:true,
            },
            1000: {
                items: 4,
                loop:true,
            },
        }            

    });
	
	
    // -------------------------------------------------------------
    //  Owl Carousel Best Selling
    // -------------------------------------------------------------



	    // -------------------------------------------------------------
    //  Owl Carousel testimonials
    // -------------------------------------------------------------
$('#testimonials').owlCarousel({
    stagePadding: 98,
    loop:true,
    margin:30,
    nav:true,
	navText: [
         "<i class='flaticon-left-arrow'></i>",
          "<i class='flaticon-right-arrow'></i>"
        ],
    responsive:{
        0:{
            items:1,
			stagePadding: 0,
        },
        600:{
            items:1,
			stagePadding: 0,
        },
        1000:{
            items:1
        }
    }
})


	    // -------------------------------------------------------------
    //  Owl Carousel brands 
    // -------------------------------------------------------------
$('#brands').owlCarousel({
    loop:true,
    margin:30,
    nav:true,
	navText: [
         "<i class='flaticon-back'></i>",
          "<i class='flaticon-next'></i>"
        ],
    responsive:{
        0:{
            items:2
        },
        600:{
            items:3
        },
        1000:{
            items:5
        }
    }
})

	    // -------------------------------------------------------------
    //  Owl Carousel Latest News
    // -------------------------------------------------------------
$('#latest_news').owlCarousel({
    loop:true,
    margin:30,
    nav:true,
	navText: [
         "<i class='flaticon-left-arrow'></i>",
          "<i class='flaticon-right-arrow'></i>"
        ],
    responsive: {
            0: {
                items: 1,
                slideBy:1
            },
			576: {
                items: 2,
            },
            768: {
                items: 2,
                slideBy:2
            },
            991: {
                items: 3,
                loop:true,
                 dots:true,
            },
            1000: {
                items: 3,
                loop:true,
            },
        }     
})

    // -------------------------------------------------------------
    //  Owl Carousel Instagram
    // -------------------------------------------------------------

    $("#instagram").owlCarousel({
        items:4,
        margin:1,
        nav:true,
        autoplay:false,
        autoplayHoverPause:true,
        loop:false,
        navText: [
         "<i class='flaticon-left-arrow'></i>",
          "<i class='flaticon-right-arrow'></i>"
        ],
        responsive: {
            0: {
                items: 1,
            },
			576: {
                items: 3,
            },
            768: {
                items: 4,
                slideBy:4
            },
            991: {
                items: 3,
                loop:true,
                 dots:true,
            },
            1000: {
                items: 5,
                loop:true,
            },
			1200: {
                items: 6,
                loop:true,
            },
        }            

    });
	

	    // -------------------------------------------------------------
    //  Owl Carousel testimonials
    // -------------------------------------------------------------
$('#testimonials-tow').owlCarousel({
    loop:true,
    margin:30,
    nav:true,
    autoplay:true,
	navText: [
         "<i class='fa fa-arrow-left'></i>",
          "<i class='fa fa-arrow-right'></i>"
        ],
    responsive:{
        0:{
            items:1
        },
        767:{
            items:1
        },
        1000:{
            items:3
        }
    }
})


	    // -------------------------------------------------------------
    //  Owl Carousel widget_selling
    // -------------------------------------------------------------

    $("#widget_selling").owlCarousel({
        items:4,
        margin:20,
        nav:true,
        autoplay:false,
        autoplayHoverPause:true,
        loop:false,
        navText: [
         "<i class='flaticon-back'></i>",
          "<i class='flaticon-next'></i>"
        ],
        responsive: {
            0: {
                items: 1,
            },
			576: {
                items: 1,
            },
            768: {
                items: 1,
                slideBy:2
            },
            991: {
                items: 1,
                loop:true,
                 dots:true,
            },
            1000: {
                items: 1,
                loop:true,
            },
        }            

    });
	
/*--
        Shop-Filter
    ---------------------*/
$(".filters").on("click", function() {
  $(".filters-area").slideToggle('slow');
   $(this).toggleClass("main");
});
	

/*--
        Modal
    ---------------------*/
$(function() {
  return $(".modal").on("show.bs.modal", function() {
    var curModal;
    curModal = this;
    $(".modal").each(function() {
      if (this !== curModal) {
        $(this).modal("hide");
      }
    });
  });
});


/*--
        Stop page jumping when links are pressed
    ---------------------*/
    $('a[href="#"]').on("click", function(e) {
         return false; 
         e.preventDefault(); 
    });
	
	
	
    /*-----------------------------------------
		product-hero point
	-------------------------------------------*/

	$(".point").on('click', function () {

        var image = $(this).attr("data-image");
        var price = $(this).attr("data-price");
        var title = $(this).attr("data-title");

        $(".product-hero .thumbnail").attr('src', image);
        $(".product-hero .product-title").text(title);
        $(".product-hero .sale-price").text(price);

		$("body").addClass('fix');
		$(".product-hero").addClass('open');
       
        

	});

	$(".point-btn-close,.body-overlay").on('click', function () {
		$("body").removeClass('fix');
		$(".product-hero").removeClass('open');
	});	


