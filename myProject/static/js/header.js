/**
 * Created by Lynn on 2016/11/21.
 */
$('.banner a').click(function () {
    var _this = $(this).parent();
    _this.siblings().removeClass('selected');
    _this.addClass('selected');
})

$('.loginButton button').click(function () {
    $('.login-layer').removeClass('hidden');
    $('.login-table').removeClass('hidden');
})
$('.dl_close').click(function () {
    $('.login-layer').addClass('hidden');
    $('.login-table').addClass('hidden');
})
$('.search-option').click(function () {
    $('.search-selection').css("display","block");
})
$('.search-selection li').click(function () {
    var _this=$(this).text();
    $('.intext').html(_this);
    $('.search-selection').css("display","none");
})

