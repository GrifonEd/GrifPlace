package com.example.grifplace;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

public class InputPasswordActivity extends AppCompatActivity {

    String id,type,password,area;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_input_password1);

        Intent intent = getIntent();
        id=intent.getStringExtra("id");
        type=intent.getStringExtra("type");
        password=intent.getStringExtra("password");
        area=intent.getStringExtra("area");

        Button button = (Button)findViewById(R.id.input);
        TextView ViewPassword = (TextView)findViewById(R.id.Password);
        ImageView imageAccess = (ImageView)findViewById(R.id.result);

        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if(password==ViewPassword.getText().toString()){
                    imageAccess.setImageResource(R.drawable.open);

                }
            }
        });
    }


}