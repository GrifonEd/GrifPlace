package com.example.grifplace;

import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class ApiClient {
    private static Retrofit getRetrofit(){
        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl("http://192.168.56.104:8000/api/docs/")
                .addConverterFactory(GsonConverterFactory.create())
                .build();

        return  retrofit;
    }

    public  static  UserService getUserService(){
        UserService userService = getRetrofit().create(UserService.class);

        return userService;
    }

    public  static  FlatService getFlatService(){
        FlatService flatService = getRetrofit().create(FlatService.class);

        return flatService;
    }

}

