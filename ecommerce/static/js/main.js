(function ($) {
    "use strict";
    
    // Dropdown on mouse hover
    $(document).ready(function () {
        function toggleNavbarMethod() {
            if ($(window).width() > 992) {
                $('.navbar .dropdown').on('mouseover', function () {
                    $('.dropdown-toggle', this).trigger('click');
                }).on('mouseout', function () {
                    $('.dropdown-toggle', this).trigger('click').blur();
                });
            } else {
                $('.navbar .dropdown').off('mouseover').off('mouseout');
            }
        }
        toggleNavbarMethod();
        $(window).resize(toggleNavbarMethod);
    });
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Vendor carousel
    $('.vendor-carousel').owlCarousel({
        loop: true,
        margin: 29,
        nav: false,
        autoplay: true,
        smartSpeed: 1000,
        responsive: {
            0:{
                items:2
            },
            576:{
                items:3
            },
            768:{
                items:4
            },
            992:{
                items:5
            },
            1200:{
                items:6
            }
        }
    });


    // Related carousel
    $('.related-carousel').owlCarousel({
        loop: true,
        margin: 29,
        nav: false,
        autoplay: true,
        smartSpeed: 1000,
        responsive: {
            0:{
                items:1
            },
            576:{
                items:2
            },
            768:{
                items:3
            },
            992:{
                items:4
            }
        }
    });


    // Product Quantity
    $('.quantity button').click(function () {
        var button = $(this);
        var oldValue = button.parent().parent().find('input').val();
        if (button.hasClass('btn-plus')) {
            var newVal = parseFloat(oldValue) + 1;
        } else {
            if (oldValue > 0) {
                var newVal = parseFloat(oldValue) - 1;
            } else {
                newVal = 0;
            }
        }
        button.parent().parent().find('input').val(newVal);
    });
    
})(jQuery);

// nav link active
$( '.nav-item .nav-link a' ).click( 
                    function () {
            $( '.nav-item .nav-link' ).find( '.nav-item .nav-link active' )
            .removeClass( '.active' );
            $( this ).parent( '.nav-item .nav-link' ).addClass( 'active' );
        });


// cart 
console.log('working');
if(localStorage.getItem('cart') == null){
    var cart = {};
}
else
{
    cart = JSON.parse(localStorage.getItem('cart'));
    document.getElementById('cart').innerHTML = Object.keys(cart).length;
}
$('.cart').click(function(){
    console.log('clicked');
    var idstr = this.id.toString();
    console.log(idstr);
    if (cart[idstr] !=undefined){
        cart[idstr] = cart[idstr] + 1;
    }
    else
    {
        cart[idstr] = 1;
    }
    console.log(cart);
    localStorage.setItem('cart', JSON.stringify(cart));
    document.getElementById('cart').innerHTML = Object.keys(cart).length;
});