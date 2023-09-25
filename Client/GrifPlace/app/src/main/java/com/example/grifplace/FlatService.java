package com.example.grifplace;

import java.util.List;

import retrofit2.Call;
import retrofit2.http.GET;

public interface FlatService {
    @GET("http://192.168.199.111:8000/api/allflat")
    Call<List<FlatResponse>> getAllFlats();
}


