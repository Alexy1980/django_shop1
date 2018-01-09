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
