package com.example.grifplace;

import android.app.ProgressDialog;
import android.content.Intent;
import android.os.Bundle;
import android.text.TextUtils;
import android.util.Patterns;
import android.view.View;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import com.example.grifplace.databinding.ActivityRegisterBinding;
//import com.google.android.gms.tasks.OnCompleteListener;
//import com.google.android.gms.tasks.OnFailureListener;
//import com.google.android.gms.tasks.OnSuccessListener;
//import com.google.android.gms.tasks.Task;


import java.util.HashMap;

public class RegisterActivity extends AppCompatActivity {

    private ActivityRegisterBinding binding;


    private ProgressDialog progressDialog;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        binding = ActivityRegisterBinding.inflate(getLayoutInflater());
        setContentView(binding.getRoot());

        progressDialog = new ProgressDialog(this);
        progressDialog.setTitle("Please wait");
        progressDialog.setCanceledOnTouchOutside(false);

        binding.registerBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                validateData();
            }
        });

        binding.backBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                onBackPressed();
            }
        });
    }
    private String name = "",email = "",password = "";
    private void validateData(){
     name = binding.nameEt.getText().toString().trim();
     email = binding.emailEt.getText().toString().trim();
     password = binding.passwordEt.getText().toString().trim();
     String cPassword = binding.cPasswordEt.getText().toString().trim();

     if(TextUtils.isEmpty(name)){
         Toast.makeText(this,"Enter your name...", Toast.LENGTH_SHORT).show();
     }
     else if(!Patterns.EMAIL_ADDRESS.matcher(email).matches()){
         Toast.makeText(this,"Invalid email adress!", Toast.LENGTH_SHORT).show();

     }
     else if(TextUtils.isEmpty(password)){
            Toast.makeText(this,"Enter password...", Toast.LENGTH_SHORT).show();

        }
     else if(TextUtils.isEmpty(cPassword)){
         Toast.makeText(this,"Confirm password!", Toast.LENGTH_SHORT).show();

     }
     else if(!password.equals((cPassword))){
         Toast.makeText(this,"Password doesn't match!", Toast.LENGTH_SHORT).show();

     }
     else {
         //createUserAccount();
     }
    }

}