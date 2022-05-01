$("#loginForm").submit(function (event) {
  event.preventDefault();
  $("#loading").addClass("loadingShow");
  request = $.ajax({
    url: "/authenticate/login",
    type: "post",
    data: {
      email: $("#email").val(),
      password: $("#password").val(),
      submit: $("#btnLog").val(),
    },
  });
  request.done(function (response, textStatus, jqXHR) {
    window.location.reload();
  });
  request.fail(function (jqXHR, textStatus, errorThrown) {
    // Log the error to the console
    $("#loading").removeClass("loadingShow");
    const error = JSON.parse(jqXHR.responseText);
    $("#loginError").html(error.message || "Login failed");
  });
});

$("#signUpForm").submit(function (event) {
  event.preventDefault();
  const data = new FormData();
  $("#loading").addClass("loadingShow");

  data.append("submit", $("#signUpBtn").attr("value"));
  data.append("email", $("#sgEmail").val());
  data.append("password", $("#sgPassword").val());
  data.append("phone", $("#sgPhone").val());
  data.append("birthday", $("#sgBirthday").val());
  data.append("name", $("#sgName").val());

  const fileList = $("#sgAvatar")[0].files;
  data.append("avatar", fileList.length > 0 ? fileList[0] : null);

  request = $.ajax({
    url: "/authenticate/signUp",
    type: "post",
    data: data,
    processData: false,
    contentType: false,
  });

  request.done(function (response, textStatus, jqXHR) {
    $("#loading").removeClass("loadingShow");
    $.snackbar({
      content: "Sign up success.Wait page reload and login",
      timeout: 5000,
      style: "customSnackbar snackbar-success",
    });
  });

  request.fail(function (jqXHR, textStatus, errorThrown) {
	  console.log( textStatus, errorThrown)
    $.snackbar({
      content: errorThrown,
      timeout: 5000,
      style: "customSnackbar snackbar-error",
    });
    $("#loading").removeClass("loadingShow");
    // $("#signupModal").modal("hide");s
  });

  // $("#signOutBtn").click(function(event) {
  //     $("#loading").addClass("loadingShow");
  //     $("#backDrop").addClass("loadingShow");
  //     request = $.ajax({
  //         url: "./ajax/authentication.php",
  //         type: "post",
  //         data: {
  //             submit: $("#signOutBtn").attr('value')
  //         },
  //     });
  //     $("#loading").removeClass("loadingShow");
  //     $("#signupModal").modal('hide');
  // });
});

$("#signOutBtn").click(function (event) {
  $("#loading").addClass("loadingShow");
  $("#backDrop").addClass("loadingShow");
  request = $.ajax({
    url: "/authenticate/signOut",
    type: "post",
    data: {
      submit: $("#signOutBtn").attr("value"),
    },
  });

  request.done(function (response, textStatus, jqXHR) {
    $("#loading").removeClass("loadingShow");
    window.location.reload();
  });
  request.fail(function (jqXHR, textStatus, errorThrown) {
    $("#loading").removeClass("loadingShow");
    $("#signupModal").modal("hide");
  });
});
