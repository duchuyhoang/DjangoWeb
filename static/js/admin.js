const selectizeSetting = {
  create: true,
  sortField: "text",
  create: false,
};

let $select,
  $newBookManufactureSelect,
  $newBookCategorySelect = null;

$(document).ready(function () {
  $select = $("#newBookAuthor").selectize({
    ...selectizeSetting,
  });
  $select[0].selectize.setValue("Search here");

  $newBookManufactureSelect = $("#newBookManufacture").selectize({
    ...selectizeSetting,
  });
  $newBookManufactureSelect[0].selectize.setValue("Search here");

  $newBookCategorySelect = $("#newBookCategory").selectize({
    ...selectizeSetting,
    maxItems: 100,
  });
  $newBookCategorySelect[0].selectize.setValue("Search here");
});

function reset() {
  $("#addBookForm").trigger("reset");
  $select[0].selectize.clear();
  $newBookManufactureSelect[0].selectize.clear();
  $newBookCategorySelect[0].selectize.clear();
}

$("#addNewProduct").click(function (event) {
  event.preventDefault();
  $("#loading").addClass("loadingShow");
  const data = new FormData();
  data.append("bookName", $("#newBookName").val());
  data.append("bookQuantity", $("#newBookQuantity").val());
  data.append("bookPrice", $("#newBookPrice").val());
  data.append("salePrice", $("#newSalePrice").val());
  data.append("bookAuthor", $select[0].selectize.getValue());
  data.append("bookDescription", $("#newBookDescription").val());
  data.append(
    "bookManufacture",
    $newBookManufactureSelect[0].selectize.getValue()
  );
  data.append("bookCategory", $newBookCategorySelect[0].selectize.getValue());

  const fileList = $("#newBookImage")[0].files;
  if (fileList.length > 0) {
    for (let i = 0; i < fileList.length; i++) {
      data.append("bookImage[]", fileList[i]);
    }
  } else if (fileList.length === 1) {
    data.append("bookImage[]", fileList["0"]);
  }
  reset();
  for (var pair of data.entries()) {
    console.log(pair[0] + ", " + pair[1]);
  }
  request = $.ajax({
  	url: "/management/handleAddBook",
  	type: "post",
  	data: data,
  	processData: false,
  	contentType: false,
  });
  request.done(function(response, textStatus, jqXHR) {
  	$.snackbar({
  		content: "Success!!!",
  		timeout: 5000,
  		style: "customSnackbar snackbar-success"
  	});
  	$("#loading").removeClass("loadingShow");
  });
  request.fail(function(jqXHR, textStatus, errorThrown) {
  	$.snackbar({
  		content: "Error!",
  		timeout: 5000,
  		style: "customSnackbar snackbar-error"
  	});
  	$("#loading").removeClass("loadingShow");
  });
});
