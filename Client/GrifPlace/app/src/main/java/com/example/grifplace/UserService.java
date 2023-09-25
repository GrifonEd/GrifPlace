package com.example.grifplace;

import java.util.List;

import retrofit2.Call;
import retrofit2.http.GET;
import retrofit2.http.Path;

public interface UserService {
@GET("http://192.168.199.111:8000/api/people/{value}")
Call<UserResponse> getOneUser(@Path("value")String value);


}
