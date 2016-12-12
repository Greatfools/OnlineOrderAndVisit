/**
 * Created by 朱耀华 on 2016/11/28.
 */

$('#navi-doctor').click(function () {
    $('#promoted-box1').addClass('hidden');
    $('#promoted-box2').addClass('hidden');
    $('#promoted-box3').addClass('hidden');
    $('#promoted-box4').removeClass('hidden');
    $('#promoted-box5').removeClass('hidden');
    $('#promoted-box6').removeClass('hidden');

    $('#navi-doctor').addClass('active');
    $('#navi-hosp').removeClass('active');
})
$('#navi-hosp').click(function () {
    $('#promoted-box4').addClass('hidden');
    $('#promoted-box5').addClass('hidden');
    $('#promoted-box6').addClass('hidden');
    $('#promoted-box1').removeClass('hidden');
    $('#promoted-box2').removeClass('hidden');
    $('#promoted-box3').removeClass('hidden');
    $('#navi-doctor').removeClass('active');
    $('#navi-hosp').addClass('active');
})
$('.ct-box-bottom-blk').hover(function () {
    var _this = $(this)
    _this.siblings().css('background-color' ,'#555555');
    _this.css('background-color','#dddddd');
})
$('#blk1').hover(function () {
    $('.content-box').css({'background-image':'url("../static/img/主页背景图3修正.png")'})
    $('.pic-box').css('background-color','#659ebc');
})
$('#blk2').hover(function () {
    $('.content-box').css({'background-image':'url("../static/img/主页背景图2修正.png")'})
    $('.pic-box').css('background-color','#7bd0cd');
})
$('#blk3').hover(function () {
    $('.content-box').css({'background-image':'url("../static/img/主页背景图1修正.png")'})
    $('.pic-box').css('background-color','#0f1a38');
})

