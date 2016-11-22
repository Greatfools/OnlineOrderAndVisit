/**
 * Created by Lynn on 2016/11/21.
 */
$('.banner a').click(function () {
    var _this = $(this).parent();
    _this.siblings().removeClass('selected');
    if (!_this.hasClass('banner')){
        _this.addClass('selected');
    }

})