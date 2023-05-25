setInterval(function () {
  $.ajax({
    url: "/get_notifications/",
    type: "POST",
    data: { check: true },

    success: function (json) {
      if (json.result) {
        $("#notify_icon").addClass("notification");
        var doc = $.parseHTML(json.notifications_list);
        $("#notifications-list").html(doc);
      }
    },
  });
}, 60000);
