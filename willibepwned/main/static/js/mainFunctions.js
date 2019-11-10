function getMessage() {
    var email = document.getElementById("Email").value;
    var username = document.getElementById("Username").value;
    var password = document.getElementById("Password").value;

    if (username == null || username == "") username = email;

    if(email && email != "" && username && username != "" && password && password != "") {
        document.getElementById("Email").value = "";
        document.getElementById("Username").value = "";
        document.getElementById("Password").value = "";

        var xhr = new XMLHttpRequest();
        xhr.open("POST", "/backend/email/", true);
        // xhr.setRequestHeader('Content-Type', 'multipart/form-data');
        var formData = new FormData();
        formData.append("username", username);
        formData.append("password", password);
        formData.append("email", email);
        // xhr.send(JSON.stringify({
        //     email: email,
        //     username: username,
        //     password: password
        // }));
        xhr.send(formData);

        var container = document.getElementById("outputMessage");
        var title = document.getElementById("yes");
        var subtitle = document.getElementById("subyes");

        // pick a random message
        title.textContent = "yes";
        title.style.fontSize = "2.5em";

        var messages = [
            "Protip: don't give your credentials to untrustworthy sites :-)",
            "Amazing! only two other users had the same password as you",
            "you dumb bitch",
            "bUt mY InTErnEt sECurItY",
            "but did you really believe this site",
            "Jeffery Epstein didn't kill himself",
            "though we can't predict the exact future",
            "why would you give us your password",
            "nothing is safe on the internet",
            "change your passwords twice a minute",
            "unless you venmo me $200",
            "now you've fucked up",
        ];
        subtitle.textContent = messages[Math.floor(Math.random() * messages.length)];
        container.style.fontSize = "1.5em";

        container.style.display = "block";
    }
  }

  function setRand(id) {
      console.log(id);
    var element = document.getElementById(id);
    console.log(element);
    if(element) element.textContent = Math.floor(Math.random() * 100000);
  }

setRand("rand1");
setRand("rand2");
setRand("rand3");
setRand("rand4");
setRand("rand5");
setRand("rand6");
setRand("rand7");
setRand("rand8");
setRand("rand9");
setRand("rand10");
setRand("rand11");
setRand("rand12");
