$(document).ready(function(){
 $(".device_toggle_state").click(function(){
        device_to_edit = $(this).attr("id");
        old_state = $(this).attr("state");
        if (old_state == 1){
            state = 0;
            $(parent).text = "0";
        } else {
            state = 1;
            $(parent).text = "1"
        }
        $.get("submit", {state: state, device_id: device_to_edit});
    });
});
