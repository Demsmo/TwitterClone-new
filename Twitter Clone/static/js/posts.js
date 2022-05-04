//////////////////////////////
// Javascript for Posts page
//////////////////////////////
$(function() {
    // executed when js-menu-icon js clicked
    $('.js-menu-icon').click(function() {
        $(this).next().toggle();
    })
})