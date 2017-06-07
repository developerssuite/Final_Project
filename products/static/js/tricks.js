$(function () {
    'use strict';
    $('.navbtn').click(function(){
      $('.topnavbar').slideToggle(250, function(){
        $('.btn-group').css('margin-top','-301px !important')
      });
    })


    $('.closeimg').click(function(){
      $('.topbar').slideUp(500, function(){
        $('.top').css('height','auto');
        $('.content .rightside').css('margin-top','-20px');

      });
    })



    $('.emailform').submit(function() {
      if($('.emailform input').val() == ''){
          alert('Please Enter valid Email!.');
          return false;
      }
  });



  $(window).scroll(function(){
      if($(this).scrollTop()>=300)
        {$(".fa-chevron-up").slideDown(1000);}
      else
        {$(".fa-chevron-up").slideUp(1000);}
    })
  $(".fa-chevron-up").click(function(){
    $("html,body").animate({scrollTop:0},500);

    })


/*  $('.xspan').click(function(){
    $('#login').slideUp(1000, function(){
      $('body').css('padding-right','0px');
      $('.modal-backdrop').removeClass('in');
      $('.modal-backdrop').removeClass('modal-backdrop');
      $('body').removeClass('modal-open');
    });
  })



  $('.dropdown-toggle').click(function(){
    $(this).css('background-color','hsl(223, 100%, 74%)')
    $(this).css('border-left','1px solid #fff')
    $(this).css('box-shadow','none')
  })
  */


  $('.editUserImg-Name').click(function(){
    $('.user-img-and-name').slideDown(500);
  })

  $('.edit-skypeid').click(function(){
    $('.skypeform').slideDown(500);
  })

  $('.cancel').click(function(){
    $(this).parent().slideUp(500);
  })

  $('.edit-language').click(function(){
    $('.flanguage').slideDown(500);
  })

  $('.edit-description').click(function(){
    $('.description').slideDown(500);
  })

  $('.edit-phone').click(function(){
    $('.phone').slideDown(500);
  })


  $('.edit-address').click(function(){
    $('.address').slideDown(500);
  })

  $('.edit-email').click(function(){
    $('.email').slideDown(500);
  })

})


var $exampleModal = $("#example-modal"),
  $exampleModalClose = $(".moda-header button");

  $exampleModal.on("shown.bs.modal", function(){
    document.activeElement.blur();
    $exampleModalClose.focus();
  });
