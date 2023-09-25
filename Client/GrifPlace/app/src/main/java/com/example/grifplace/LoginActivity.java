package com.example.grifplace;

import android.app.ProgressDialog;
import android.content.Intent;
import android.os.Bundle;
import android.text.Editable;
import android.text.TextUtils;
import android.text.TextWatcher;
import android.util.Log;
import android.util.Patterns;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import com.example.grifplace.databinding.ActivityLoginBinding;
import com.example.grifplace.databinding.FragmentBookUserBinding;

import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
//import com.google.android.tasks.OnFailureListener;
//import com.google.android.gms.tasks.OnSuccessListener;


public class LoginActivity extends AppCompatActivity {

    private ActivityLoginBinding binding;


private ProgressDialog progressDialog;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        binding = ActivityLoginBinding.inflate(getLayoutInflater());
        setContentView(binding.getRoot());


        progressDialog = new ProgressDialog(this);
        progressDialog.setTitle("Please wait");
        progressDialog.setCanceledOnTouchOutside(false);

        binding.noAccountTv.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                startActivity(new Intent(com.example.grifplace.LoginActivity.this, com.example.grifplace.RegisterActivity.class));
            }
        });

        binding.backloginBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                onBackPressed();
            }
        });


        binding.loginBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                validateData();
            }


        });



        }



    private String passport = "",password = "";



    private void validateData() {

        passport = binding.emailEt2.getText().toString();
        password = binding.passwordEt2.getText().toString();

        Call<UserResponse> UserList = ApiClient.getUserService().getOneUser(passport);
        UserList.enqueue(new Callback<UserResponse>()  {
            @Override
            public void onResponse(Call<UserResponse> call, Response<UserResponse> response) {
                if (response.isSuccessful())
                {
                    Log.e("success", response.body().toString());
                        if(response.body().getPassport_number().toString().equals(passport))
                        {
                            if(response.body().getPassword().toString().equals(password))
                            {
                                Intent intent = new Intent(LoginActivity.this,FlatsActivity.class) ;
                                intent.putExtra("passport", passport);
                                startActivity(intent);
                                finish();
                            }
                        else{
                                Log.e("no password ", response.body().getPassword().toString() + " "+ password);
                            }
                        }
                        else{
                            Log.e("no passport ", response.body().getPassport_number().toString() + " "+ passport);
                        }
                }
                else {
                    Log.e("success","что делать?");
                }
            }

            @Override
            public void onFailure(Call<UserResponse> call, Throwable t) {

            }




        });


    }






}
