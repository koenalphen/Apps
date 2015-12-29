$(document).ready(function(){
 $(".device_toggle_state").click(function(){
        device_to_edit = $(this).attr("id");
        old_state = $(this).attr("state");
        if (old_state == 1){
            state = 0;
            $(parent).text = "0";
            $(this).attr("state") = "0";
        } else {
            state = 1;
            $(parent).text = "1";
            $(this).attr("state") = "1";
        }
 });
});
