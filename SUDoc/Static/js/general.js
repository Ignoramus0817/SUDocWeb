function mainRegisterClick(){
	document.getElementById("loginModule").style.display = "none"; 
	document.getElementById("resetModule").style.display = "none";
	document.getElementById("registerModule").style.display = "";
	document.getElementById("userID").value = "";
	document.getElementById("password").value = "";
	document.getElementById("userResetEmail").value = "";
}

function mainResetClick(){
	document.getElementById("loginModule").style.display = "none"; 
	document.getElementById("registerModule").style.display = "none";
	document.getElementById("resetModule").style.display = "";
	document.getElementById("userID").value = "";
	document.getElementById("password").value = "";
	document.getElementById("userRegID").value = "";
	document.getElementById("userRegFirstName").value = "";
	document.getElementById("userRegLastName").value = "";
	document.getElementById("userRegEmail").value = "";
	document.getElementById("userRegConfirmPassword").value = "";
	document.getElementById("userRegPassword").value = "";
}

function browserClick(){
	document.getElementById("userID").value = "";
	document.getElementById("password").value = "";
	document.getElementById("userRegID").value = "";
	document.getElementById("userRegFirstName").value = "";
	document.getElementById("userRegLastName").value = "";
	document.getElementById("userRegEmail").value = "";
	document.getElementById("userRegConfirmPassword").value = "";
	document.getElementById("userRegPassword").value = "";
	document.getElementById("userResetEmail").value = "";
	window.location.href = "/filebrowser/";
}

function registerCancel(){
	document.getElementById("loginModule").style.display = ""; 
	document.getElementById("registerModule").style.display = "none";
	document.getElementById("userRegID").value = "";
	document.getElementById("userRegFirstName").value = "";
	document.getElementById("userRegLastName").value = "";
	document.getElementById("userRegEmail").value = "";
	document.getElementById("userRegConfirmPassword").value = "";
	document.getElementById("userRegPassword").value = "";
}

function resetCancel(){
	document.getElementById("loginModule").style.display = ""; 
	document.getElementById("resetModule").style.display = "none";
	document.getElementById("userResetEmail").value = "";
}

$(document).ready(function(){
	$('#loginForm').submit(function(){
		var userID = $('#userID').val();
		var password = $('#password').val();
		
		$.ajax({
			type:"POST",
			data:{userID:userID,
				  password:password},
			cache:false,
			dataType:"html",
			success:function(result){
				if(result == ['success'])
					window.location.href = "/filebrowser/"
				else{
					var alertMessage = "";
					for(var i = 0; i < JSON.parse(result).length; i++)
						alertMessage += JSON.parse(result)[i] + "!\n";
					alert(alertMessage);
				}
			},
			error:function(XMLHttpResponse, textStatus, errorThrown){
                console.log("1 异步调用返回失败,XMLHttpResponse.readyState:"+XMLHttpResponse.readyState);
                console.log("2 异步调用返回失败,XMLHttpResponse.status:"+XMLHttpResponse.status);
                console.log("3 异步调用返回失败,textStatus:"+textStatus);
                console.log("4 异步调用返回失败,errorThrown:"+errorThrown);
			}
		});
		return false;
	});
	
	$('#registerForm').submit(function(){
		var userRegID = $('#userRegID').val();
		var userRegLastName = $('#userRegLastName').val();
		var userRegFirstName = $('#userRegFirstName').val();
		var userRegEmail = $('#userRegEmail').val();
		var userRegPassword = $('#userRegPassword').val();
		var userRegConfirmPassword = $('#userRegConfirmPassword').val();
			
		$.ajax({
			type:"POST",
			data:{userRegID:userRegID,
				  userRegLastName:userRegLastName,
				  userRegFirstName:userRegFirstName,
				  userRegEmail:userRegEmail,
				  userRegPassword:userRegPassword,
				  userRegConfirmPassword:userRegConfirmPassword},
			cache:false,
			dataType:"html",
			success:function(result){
				// dirty process method
				if(result == ['success'])
					alert("激活邮件已发送，请注意查收");
				else{
					var alertMessage = "";
					for(var i = 0; i < JSON.parse(result).length; i++)
						alertMessage += JSON.parse(result)[i] + "!\n";
					alert(alertMessage);
				}
			},
			error: function(XMLHttpResponse, textStatus, errorThrown){
                console.log("1 异步调用返回失败,XMLHttpResponse.readyState:"+XMLHttpResponse.readyState);
                console.log("2 异步调用返回失败,XMLHttpResponse.status:"+XMLHttpResponse.status);
                console.log("3 异步调用返回失败,textStatus:"+textStatus);
                console.log("4 异步调用返回失败,errorThrown:"+errorThrown);
			}
		});
		return false;
	});
	
	$("#uploadForm").submit(function(){
		var formData = new FormData();
		var file = $('#userFile')[0].files[0];
		formData.append('userFile', file);
		
		$.ajax({
			url: "/filebrowser/",
			cache: false,
			type: "POST",
			data: formData,
			dataType:'html',
			contentType: false,
			processData: false,
			success: function(result){
				if(result == ['success'])
					alert("上传成功");
				else{
					console.log(result);
//					var alertMessage = "";
//					for(var i = 0; i < JSON.parse(result).length; i++)
//						alertMessage += JSON.parse(result)[i] + "!\n";
//					alert(alertMessage);
					console.log(file);
				}
			},
			error:function(XMLHttpResponse, textStatus, errorThrown){
                console.log("1 异步调用返回失败,XMLHttpResponse.readyState:"+XMLHttpResponse.readyState);
                console.log("2 异步调用返回失败,XMLHttpResponse.status:"+XMLHttpResponse.status);
                console.log("3 异步调用返回失败,textStatus:"+textStatus);
                console.log("4 异步调用返回失败,errorThrown:"+errorThrown);
			}
		});
		return false;
	});
	
});

function uploadWindow(){
	document.getElementById("fileUploadJumbo").style.display = "";
}

function uploadCancel(){
	document.getElementById("fileUploadJumbo").style.display = "none";
}

function browserBack(){
	window.location.href = "/";
}

function thanksToMain(){
	setTimeout("javascript:location.href = '/'", 2000);
}
