$(document).ready(function(){
    var form = $('#form_buying_product');

    function basketUpdating(product_id, nmb, is_delete){
        var data = {};
        data.product_id = product_id;
        data.nmb = nmb;
         var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
        if(csrf_token){
           data["csrfmiddlewaretoken"] = csrf_token;
        } else {
           data["csrfmiddlewaretoken"] = $('#token [name="csrfmiddlewaretoken"]').val();
        }
        // проверяем, передано ли is_delete
        if (is_delete){
            data["is_delete"] = true;
        }

         var url = form.attr("action");

        console.log(data);
         $.ajax({
             url: url,
             type: 'POST',
             data: data,
             cache: true,
             success: function (data) {
                 console.log("OK");
                 console.log(data.products_total_nmb);
                 if (data.products_total_nmb || data.products_total_nmb == 0){
                    $('#basket_total_nmb').text("("+data.products_total_nmb+")");
                     // console.log(data.products);
                     $('.basket-items ul').html("");
                     $.each(data.products, function(k, v){
                        $('.basket-items ul').append('<li>'+ v.name+', ' + v.nmb + 'шт. ' + 'по ' + v.price_per_item + 'RUB  ' +
                            '<a class="delete-item" href="" data-product_id="'+v.id+'">x</a>'+
                            '</li>');
                     });
                 }

             },
             error: function(){
                 console.log("error")
             }
         })

    }

    form.on('submit', function(e){
        e.preventDefault();
        // console.log('123');
        var nmb = $('#number').val();
        console.log(nmb);
        var submit_btn = $('#submit_btn');
        var product_id =  submit_btn.data("product_id");
        var name = submit_btn.data("name");
        var price = submit_btn.data("price");
        console.log(product_id );
        console.log(name);

        basketUpdating(product_id, nmb, is_delete=false)

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
        var product_id = $(this).data("product_id");
        var nmb = 0;
        // удаляем ближайший элемент li
        // $(this).closest('li').remove();
        basketUpdating(product_id, nmb, is_delete=true);
    });

    function calculatingBasketAmount(){
        var total_order_amount = 0;
        $('.total_product_in_basket_amount').each(function(){
            total_order_amount += parseFloat($(this).text());
        });
        // console.log(total_order_amount);
        // вписываем сумму заказа в span
        $('#total_order_amount').text(total_order_amount.toFixed(2));
    }
    // отслеживаем изменение поля количества
    $(document).on('change', '.product_in_basket_nmb', function(){
        var current_nmb = $(this).val();
        // ищем ближайшую строку к полю input
        var current_tr = $(this).closest('tr');
        var current_price = parseFloat(current_tr.find('.product_price').text()).toFixed(2);
        var total_amount = parseFloat(current_nmb*current_price).toFixed(2);
        current_tr.find('.total_product_in_basket_amount').text(total_amount);
        console.log(total_amount);
        calculatingBasketAmount();
    });

    calculatingBasketAmount();
});
