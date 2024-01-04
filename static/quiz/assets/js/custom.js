// next prev
var divs = $(".show-section fieldset");
var button = $(".nextPrev");
var now = 0; // currently shown div
divs.hide().first().show(); // hide all divs except first
button.hide().first().show(); // hide all divs except first

function next() {
  divs.eq(now).hide();
  now = now + 1 < divs.length ? now + 1 : 0;
  divs.eq(now).show(); // show next
  console.log(now);

  $(".stepSingle").removeClass("active");
  $(".stepSingle").eq(now).addClass("active");

  button.hide().eq(now).show();
}
$(".prev").on("click", function () {
  divs.eq(now).hide();
  now = now > 0 ? now - 1 : divs.length - 1;
  divs.eq(now).show(); // show previous
  console.log(now);

  button.hide().eq(now).show();

  $(".option").addClass("animate");
  $(".option").removeClass("animateReverse");

  $(".stepSingle").removeClass("active");
  $(".stepSingle").eq(now).addClass("active");
});

// quiz validation
var checkedradio = false;

function radiovalidate(stepnumber) {
  var checkradio = $("#step" + stepnumber + " input")
    .map(function () {
      if ($(this).is(":checked")) {
        return true;
      } else {
        return false;
      }
    })
    .get();

  checkedradio = checkradio.some(Boolean);
}

$(document).ready(function () {
  $(".stepSingle").eq(0).addClass("active");

  // check step1
  $("#step1btn").on("click", function () {
    radiovalidate(1);

    if (checkedradio == false) {
      (function (el) {
        setTimeout(function () {
          el.children().remove(".reveal");
        }, 3000);
      })(
        $("#error").append(
          '<div class="reveal alert alert-danger">Выберите один из предложенных вариант!</div>'
        )
      );

      radiovalidate(1);
    } else {
      $("#step1 .option").removeClass("animate");
      $("#step1 .option").addClass("animateReverse");
      setTimeout(function () {
        next();
      }, 900);
      // countresult(1);
    }
  });
  // check step2
  $("#step2btn").on("click", function () {
    radiovalidate(2);

    if (checkedradio == false) {
      (function (el) {
        setTimeout(function () {
          el.children().remove(".reveal");
        }, 3000);
      })(
        $("#error").append(
          '<div class="reveal alert alert-danger">Выберите один из предложенных вариант!</div>'
        )
      );

      radiovalidate(2);
    } else {
      $("#step2 .option").removeClass("animate");
      $("#step2 .option").addClass("animateReverse");
      setTimeout(function () {
        next();
      }, 900);
      // countresult(1);
    }
  });
  // check step3
  $("#step3btn").on("click", function () {
    radiovalidate(3);

    if (checkedradio == false) {
      (function (el) {
        setTimeout(function () {
          el.children().remove(".reveal");
        }, 3000);
      })(
        $("#error").append(
          '<div class="reveal alert alert-danger">После того как написали нажмите на кнопку - закончил(а)  </div>'
        )
      );

      radiovalidate(3);
    } else {
      $("#step3 .option").removeClass("animate");
      $("#step3 .option").addClass("animateReverse");
      setTimeout(function () {
        next();
      }, 900);
      // countresult(1);
    }
  });
  // check step4
  $("#step4btn").on("click", function () {
    radiovalidate(4);

    if (checkedradio == false) {
      (function (el) {
        setTimeout(function () {
          el.children().remove(".reveal");
        }, 3000);
      })(
        $("#error").append(
          '<div class="reveal alert alert-danger">Выберите один из предложенных вариант!</div>'
        )
      );

      radiovalidate(4);
    } else {
      $("#step4 .option").removeClass("animate");
      $("#step4 .option").addClass("animateReverse");
      setTimeout(function () {
        next();
      }, 900);
      // countresult(1);
    }
  });
  // check step5
  $("#sub").on("click", function () {
    radiovalidate(5);

    if (checkedradio == false) {
      (function (el) {
        setTimeout(function () {
          el.children().remove(".reveal");
        }, 3000);
      })(
        $("#error").append(
          '<div class="reveal alert alert-danger">Выберите один из предложенных вариант!</div>'
        )
      );

      radiovalidate(5);
    } else {
      const inputResult = document.getElementById('quiz_result')
      const input1 = document.querySelectorAll('#step1 input[type=radio]')
      for (let i = 0; i < input1.length; i++) {
        if(input1[i].checked===true){
          inputResult.value += `quiz1:${input1[i].value}|`
        }
      }
      const input2 = document.querySelectorAll('#step2 input[type=radio]')
      for (let i = 0; i < input2.length; i++) {
        if(input2[i].checked===true){
          inputResult.value += `quiz2:${input2[i].value}|`
        }
      }
      const input3 = document.querySelectorAll('#step3 input[type=radio]')
      for (let i = 0; i < input3.length; i++) {
        if(input3[i].checked===true){
          inputResult.value += `quiz3:${input3[i].value}|`
        }
      }
      const input4 = document.querySelectorAll('#step4 input[type=radio]')
      for (let i = 0; i < input4.length; i++) {
        if(input4[i].checked===true){
          inputResult.value += `quiz4:${input4[i].value}|`
        }
      }
      const input5 = document.querySelectorAll('#step5 input[type=radio]')
      for (let i = 0; i < input5.length; i++) {
        if(input5[i].checked===true){
          inputResult.value += `quiz5:${input5[i].value}|`
        }
      }
      console.log(inputResult.value);

      showresult();
    }
  });
});
