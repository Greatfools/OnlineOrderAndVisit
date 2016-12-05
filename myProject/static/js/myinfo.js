/**
 * Created by Kevin on 2016/12/6.
 */
// var switchbool = false;
var changePWBtnDom = document.getElementById("changePWBtn");
var myInfoBtnDom = document.getElementById("myInfoBtn");
var changePWDom = document.getElementById("changePWForm");
var myInfoCntntDom = document.getElementById("myInfoCntntDiv");
function onload(){
    switchbool = false;
    changePWDom.style.display="none";
}
function myInfoCntntDis(){
    changePWDom.style.display="none";
    myInfoCntntDom.style.display="block";
    changePWBtnDom.className="btn col-md-2 col-lg-2 myInfoLblUnSelected";
    myInfoBtnDom.className="btn col-md-2 col-lg-2 myInfoLblSelected";
}
function changePWDis(){
    changePWDom.style.display="block";
    myInfoCntntDom.style.display="none";
    changePWBtnDom.className="btn col-md-2 col-lg-2 myInfoLblSelected";
    myInfoBtnDom.className="btn col-md-2 col-lg-2 myInfoLblUnSelected";
}