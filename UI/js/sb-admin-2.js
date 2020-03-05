(function($) {
  "use strict"; // Start of use strict

  //LANGUAGE
  /*
  var test = $.getJSON(test.json); var jsontest = JSON.parse(test);
  console.log(jsontest);
  */console.log(langJso);
    var arrLang =  langJso;
    console.log(arrLang);
    // The default language is Englis
    var lang = "en-gb";
     // Check for localStorage support
    if('localStorage' in window){       
       var usrLang = localStorage.getItem('uiLang');
       if(usrLang) {lang = usrLang}
    }
        $(document).ready(function() {

          $(".lang").each(function(index, element) {
            $(this).text(arrLang[lang][$(this).attr("key")]);
          });
        });

        // get/set the selected language
        $(".translate").click(function() {
          var lang = $(this).attr("id");

          // update localStorage key
          if('localStorage' in window){
               localStorage.setItem('uiLang', lang);
               console.log( localStorage.getItem('uiLang') );
          }

          $(".lang").each(function(index, element) {
            $(this).text(arrLang[lang][$(this).attr("key")]);
          });
        });

  // get/set the selected language
  $(".translate").click(function() {
    var lang = $(this).attr("id");

    $(".lang").each(function(index, element) {
      $(this).text(arrLang[lang][$(this).attr("key")]);
    });
  });

  // Toggle the side navigation
  $("#sidebarToggle, #sidebarToggleTop").on('click', function(e) {
    $("body").toggleClass("sidebar-toggled");
    $(".sidebar").toggleClass("toggled");
    if ($(".sidebar").hasClass("toggled")) {
      $('.sidebar .collapse').collapse('hide');
    };
  });

  // Close any open menu accordions when window is resized below 768px
  $(window).resize(function() {
    if ($(window).width() < 768) {
      $('.sidebar .collapse').collapse('hide');
    };
  });

  // Prevent the content wrapper from scrolling when the fixed side navigation hovered over
  $('body.fixed-nav .sidebar').on('mousewheel DOMMouseScroll wheel', function(e) {
    if ($(window).width() > 768) {
      var e0 = e.originalEvent,
        delta = e0.wheelDelta || -e0.detail;
      this.scrollTop += (delta < 0 ? 1 : -1) * 30;
      e.preventDefault();
    }
  });

  // Scroll to top button appear
  $(document).on('scroll', function() {
    var scrollDistance = $(this).scrollTop();
    if (scrollDistance > 100) {
      $('.scroll-to-top').fadeIn();
    } else {
      $('.scroll-to-top').fadeOut();
    }
  });

  // Smooth scrolling using jQuery easing
  $(document).on('click', 'a.scroll-to-top', function(e) {
    var $anchor = $(this);
    $('html, body').stop().animate({
      scrollTop: ($($anchor.attr('href')).offset().top)
    }, 1000, 'easeInOutExpo');
    e.preventDefault();
  });

})(jQuery); // End of use strict
