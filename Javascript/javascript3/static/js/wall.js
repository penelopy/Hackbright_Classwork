$(document).ready(function () {
    // Normally, JavaScript runs code at the time that the <script>
    // tags loads the JS. By putting this inside a jQuery $(document).ready()
    // function, this code only gets run when the document finishing loading.

    $("#message-form").submit(handleFormSubmit);
    getMessages();
    // $("#clear-form").submit(clearMsgs);

    $("#message-clear").click(function(e) {
        $.get("api/wall/clear", function (response) {
            formatMsg(response);
        });

    });

});


/**
 * Handle submission of the form.
 */
function handleFormSubmit(evt) {
    evt.preventDefault();

    var textArea = $("#message");
    var msg = textArea.val();

    console.log("handleFormSubmit: ", msg);
    addMessage(msg);

    // Reset the message container to be empty
    textArea.val("");

    // prevent re-submission
    $("#message-send").prop("disabled", true);
    setTimeout(function() {
        $("#message-send").prop("disabled", false);
    }, 5000);


}

/**
 * Makes AJAX call to the server and the message to it.
 */

function formatMsg(response) {
    $("ul#message-container").empty();
    for (var i = 0; i < response["messages"].length; i++) {
        $("ul#message-container").append("<li class='list-group-item'>" + response["messages"][i]["message"] + "</li>");
    }
}

function addMessage(msg) {

    if (msg.length === 0) {
        msg = "";
    }

    else if (msg.length > 1){
        msg = $("<div>" + msg + "</div>");
        msg = msg.text();
    }

    $.post(
        "/api/wall/add",
        {'m': msg},
        function (data) {
            // formatMsg(data);
            // console.log("addMessage: ", data);
            if (data.result != "Message Received") {
                //show red error message
                $("#sent-result").removeClass("alert-info").addClass("alert-danger");
            }
            else {
                formatMsg(data);
            }
            displayResultStatus(data.result);
        }
        );


}

function getMessages() {
  $.get("/api/wall/list", function (response) {
    formatMsg(response);
  });
}

// THIS DIDN'T WORK AT ALL
    // function clearMsgs(evt) {
        
    //     // alert("I will act now!");
    //     $.get("/api/wall/clear", formatMsg(response));
    //     // console.log("cleared");
    // }

/**
 * This is a helper function that does nothing but show a section of the
 * site (the message result) and then hide it a moment later.
 */
function displayResultStatus(resultMsg) {
    var notificationArea = $("#sent-result");
    notificationArea.text(resultMsg);
    notificationArea.slideDown(function () {
        // In JavaScript, "this" is a keyword that means "the object this
        // method or function is called on"; it is analogous to Python's
        // "self". In our case, "this" is the #sent-results element, which
        // is what slideDown was called on.
        //
        // However, when setTimeout is called, it won't be called on that
        // same #sent-results element--"this", for it, wouldn't be that
        // element. We could put inside of our setTimeout call the code
        // to re-find the #sent-results element, but that would be a bit
        // inelegant. Instead, we'll use a common JS idiom, to set a variable
        // to the *current* definition of self, here in this outer function,
        // so that the inner function can find it and where it will have the
        // same value. When stashing "this" into a new variable like that,
        // many JS programmers use the name "self"; some others use "that".
        var self = this;

        setTimeout(function () {
            $(self).slideUp();
        }, 2000);
    });

    // getMessages();
}