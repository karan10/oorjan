hide_page=true;
django.jQuery(document).ready(function(){
    if (django.jQuery('#id_schedule_email').is(':checked')) {
        django.jQuery(".field-email_time").show();
        hide_page=false;
    }else
    {
        django.jQuery(".field-email_time").hide();
        hide_page=true;

    }
    django.jQuery("#id_schedule_email").click(function(){
        hide_page=!hide_page;
        if(hide_page)
        {
            django.jQuery(".field-email_time").hide();
        }else
        {
            django.jQuery(".field-email_time").show();
        }
    })
})






hide_page=true;
django.jQuery(document).ready(function(){
    if (django.jQuery('#id_test_email').is(':checked')) {
        django.jQuery(".field-test_account").show();
        hide_page=false;
    }else
    {
        django.jQuery(".field-test_account").hide();
        hide_page=true;

    }
    django.jQuery("#id_test_email").click(function(){
        hide_page=!hide_page;
        if(hide_page)
        {
            django.jQuery(".field-test_account").hide();
        }else
        {
            django.jQuery(".field-test_account").show();
        }
    })
})
