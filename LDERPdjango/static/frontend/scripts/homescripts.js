var hideboolstud = true;
var hideboolteach = true;
var hideloginpane = true;
function teacher(){
  if(hideboolstud){
    $("#sbut").hide();
    hideboolstud = false;
  }
  else{
    $("#sbut").show();
    hideboolstud = true;
  }
}

function student(){
  if(hideboolteach){
    $("#tbut").hide();
    hideboolteach = false;
  }
  else{
    $("#tbut").show();
    hideboolteach = true;
  }
}

$(function(){
$("#tform").show();
$("#sform").hide();
$("#formspace").hide();

    $("#tbut").on("click", function(){
        $("#collapse, #formspace").toggle();

    });
    $("#sbut").on("click", function(){
        $("#collapse, #sform").toggle();
    });
    $("#login_pane").on("click", function(){
        $("#tform, #sform").toggle();
    });
    $("#reg_pane").on("click", function(){
        $("#sform ,#tform").toggle();
    });
});
