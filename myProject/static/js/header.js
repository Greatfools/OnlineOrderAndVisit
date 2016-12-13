/**
 * Created by Lynn on 2016/11/21.
 */
var isOpen=0;
$(window).click(function () {
    if(isOpen=1){
        $('.search-selection').css("display","none");
        isOpen=0;
    }
})
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
$('.search-option').click(function (event) {
    if(isOpen==0){
        $('.search-selection').css("display","block");
        isOpen=1;
    }else
    {
        $('.search-selection').css("display","none");
        isOpen=0;
    }

    event.stopPropagation();
    //阻止事件冒泡的两种方式，当点击消失出现bug时请更换方式（不支持IE）
    //return false;
})
$('.search-selection li').click(function () {
    var _this=$(this).text();
    var value0='h';
    value0=$(this).attr('value');
    $('#selection').attr('value',value0);

    $('.intext').html(_this);
    $('.search-selection').css("display","none");
    isOpen=0;
})

