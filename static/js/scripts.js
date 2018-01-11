$(document).ready(function(){
    var form = $('#form_buying_product');
    // console.log(form);
    form.on('submit', function(e){
        e.preventDefault();
        var nmb = $('#number').val();
        var submit_button = $('#submit_btn');
        // считываем данные с кнопки
        var product_id = submit_button.data('product_id');
        var product_name = submit_button.data('product_name');
        var product_price = submit_button.data('product_price');

        // ajax
        var data = {};
        data.product_id = product_id;
        data.nmb = nmb;
        data.product_name = product_name;
        var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;
        var url = form.attr('action');
        // console.log(data);
        $.ajax({
             url: url,
             type: 'POST',
             data: data,
             cache: true,
             success: function (data) {
                 console.log("OK");
                 console.log(data.products_total_nmb);
                 if(data.products_total_nmb){
                     // вписываем в span id = "busket_total_nmb" значение data.products_total_nmb
                     $('#basket_total_nmb').text("(" + data.products_total_nmb + ")");
                 }
             },
             error: function(){
                 console.log("error")
             }
         });

        $('.basket-items ul').append('<li>' + product_name + ' ' + nmb + ' шт. ' + 'по ' + product_price + ' руб. ' + '<a class="delete-item" href="">x</a>' + '</li>');
    });

    function showBasket(){
        $('.basket-items').removeClass('hidden');
    }

    function closeBasket(){
        $('.basket-items').addClass('hidden');
    }

    /*$('.basket-container').on('click', function(e){
        e.preventDefault();
        showBasket();
    });*/

    $('.basket-container').mouseover(function(){
        showBasket();
    });

    $('.basket-container').mouseout(function(){
        closeBasket();
    });

    $(document).on('click', '.delete-item', function(e){
        e.preventDefault();
        // удаляем ближайший элемент li
        $(this).closest('li').remove();
    });
});
