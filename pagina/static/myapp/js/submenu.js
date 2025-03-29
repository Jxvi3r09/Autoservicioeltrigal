$(document).ready(function () {
  $(".nav-item > a").on("click", function (e) {
    var $this = $(this);

    if ($this.next(".nav-treeview").length) {
      e.preventDefault();

      $this.next(".nav-treeview").slideToggle();

      $this.find(".right").toggleClass("fa-angle-left fa-angle-down");
    }
  });
});
