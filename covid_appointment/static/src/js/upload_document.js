odoo.define('covid_appointment.upload_document_form', function (require) {
'use strict';

    var ajax = require('web.ajax');

    $(document).ready(function() {
        $('.check_postive').css('display', 'none');
        $('.not_achived_reason').css('display', 'none');
        $('#is_test_achived_yes').on('click', function(){
            $('.check_postive').css('display', 'table-row');
            $('.not_achived_reason').css('display', 'none');
        });
        $('#is_test_achived_no').on('click', function(){
            $('.check_postive').css('display', 'none'); 
            $('.not_achived_reason').css('display', 'table-row');
        });
    })

});