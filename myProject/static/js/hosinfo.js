/**
 * Created by Kevin on 2016/12/8.
 */
var hosClassTitleDom = document.getElementsByClassName("hosClassTitle");
var hosClassCntntDom = document.getElementsByClassName("hosClassCntnt");
function load() {
    $(".hosClassTitle").each(function () {
        $(this).css("paddingTop",($(this).next().height()-$(this).height())/2);
        $(this).css("paddingBottom",($(this).next().height()-$(this).height())/2);
    })
    //alert($("hosImg").height());
    //alert($("#hosInfoSim").height());
    $("#hosImg").height($("#hosInfoSim").height());
}