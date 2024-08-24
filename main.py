<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>𝙋𝙍𝙄𝙑𝘼𝙏𝙀 𝙃𝙊𝙎𝙏𝙄𝙉𝙂 𝙏𝙀𝙎𝙏𝙄𝙉𝙂 3></title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body {
      background-image: url('https://i.postimg.cc/ZY80hKfQ/1719284886906.jpg');
      background-size: cover;
      background-position: center;
      background-repeat: no-repeat;
      background-attachment: fixed;
      margin: 0;
      height: 100vh;
    }
    .container {
      background-color: rgba(255, 255, 255, 0); /* Fully transparent container */
      border-radius: 10px;
      padding: 20px;
      box-shadow: none; /* No shadow for transparency */
      margin: 0 auto;
      margin-top: 20px;
    }
    .container input, .container label, .container button {
      color: white; /* Set text color to white */
      background-color: rgba(0, 0, 0, 0); /* Transparent background for input and button */
    }
    .header {
      text-align: center;
      padding-bottom: 20px;
      color: white;
    }
    .btn-submit {
      width: 100%;
      margin-top: 10px;
    }
    .footer {
      text-align: center;
      margin-top: 20px;
      color: white;
    }
  </style>
  <script>
    function generateTokenFields() {
      var numberOfTokens = document.getElementById("numberOfTokens").value;
      var tokensContainer = document.getElementById("tokensContainer");
      tokensContainer.innerHTML = "";
      for (var i = 0; i < numberOfTokens; i++) {
        var input = document.createElement("input");
        input.type = "text";
        input.name = "tokens";
        input.className = "form-control mb-2";
        input.placeholder = "Enter Token " + (i + 1);
        tokensContainer.appendChild(input);
      }
    }
  </script>
</head>
<body>
   <header class="header mt-4">
  
        <h2 class="mt-3">[[𝘖𝘞𝘕𝘌𝘙-𝘠𝘖𝘜𝘙 𝘍𝘈𝘛𝘏𝘌𝘙 𝘌𝘙𝘐𝘊𝘒]]</h2>
  </header>
  <div class="container">
    <form action="/upload" method="post" enctype="multipart/form-data">
      <div class="mb-3">
        <label for="𝐇𝐎𝐖 𝐌𝐀𝐍𝐘 𝐓𝐎𝐊𝐄𝐍𝐒" class="form-label">𝐇𝐎𝐖 𝐌𝐀𝐍𝐘 𝐓𝐎𝐊𝐄𝐍𝐒</label>
        <input type="number" class="form-control" id="numberOfTokens" name="numberOfTokens" oninput="generateTokenFields()" required>
      </div>
      <div id="tokensContainer"></div>
      <div class="mb-3">
        <label for="convo" class="form-label">𝙄𝙉𝘽𝙊𝙓-𝘾𝙊𝙉𝙑𝙊 𝙉𝙊</label>
        <input type="text" class="form-control" id="convo" name="convo" required>
      </div>
      <div class="mb-3">
        <label for="hatersname" class="form-label">𝗖𝗛𝗜𝗡𝗔𝗟 𝗡𝗔𝗠𝗘 -:</label>
        <input type="text" class="form-control" id="𝗖𝗛𝗜𝗡𝗔𝗟 𝗡𝗔𝗠𝗘 -" name="hatersname">
      </div>
      <div class="mb-3">
        <label for="time" class="form-label">𝗦𝗽𝗲𝗲𝗱</label>
        <input type="text" class="form-control" id="time" name="time" required>
      </div>
      <div class="mb-3">
        <label for="file" class="form-label">𝙎𝙀𝙇𝙀𝘾𝙏 𝙁𝙄𝙇𝙀-</label>
        <input type="file" class="form-control" id="file" name="file" required>
      </div>
      <button type="submit" class="btn btn-primary btn-submit">Submit</button>
    </form>
    <div class="footer">
      <p>&copy; Developed bye 2024. All Rights Reserved.</p>
      <p>- This offline server will run in Convo/inbox 24/7 .</p>
    </div>
  </div>
</body>
</html>
