/**
 * Created by 朱耀华 on 2016/11/28.
 */
$(function () {
    $('.header').load('header.html');
})
$(function () {
    $('.footer').load('footer.html');
})
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