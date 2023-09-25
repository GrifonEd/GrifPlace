package com.example.grifplace;

import android.content.Intent;
import android.os.Bundle;
import android.text.Editable;
import android.text.TextWatcher;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;

import com.example.grifplace.databinding.FragmentBookUserBinding;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

/**
 * A simple {@link Fragment} subclass.
 * Use the {@link com.example.grifplace.BookUserFragment#newInstance} factory method to
 * create an instance of this fragment.
 */
public class BookUserFragment extends Fragment {
    private String area="";
    private String id="";
    private String password="";
   private String type;
    private ArrayList<ModelPdf> pdfArrayList;
    private FragmentBookUserBinding binding;
    private AdapterPdfUser adapterPdfUser;
    private  static final String TAG = "BOOKS_USER_TAG";

    public BookUserFragment() {
        // Required empty public constructor
    }


    public static com.example.grifplace.BookUserFragment newInstance(String type,String area,String id,String password) {
        com.example.grifplace.BookUserFragment fragment = new com.example.grifplace.BookUserFragment();
        Bundle args = new Bundle();
        args.putString("type",type);
        args.putString("area",area);
        args.putString("id",id);
        args.putString("password",password);
        fragment.setArguments(args);
        return fragment;
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        if (getArguments() != null) {
            type = getArguments().getString("type");
            area = getArguments().getString("area");
            id = getArguments().getString("id");
            password = getArguments().getString("password");
        }
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        binding = FragmentBookUserBinding.inflate(LayoutInflater.from(getContext()),container,false);

        Log.d(TAG,"onCreateView: ");
        loadAllFlats();

        return binding.getRoot();
    }

    private void loadAllFlats() {
        pdfArrayList = new ArrayList<>();
        String[] responce = {""};

        Call<List<FlatResponse>> flatlist = ApiClient.getFlatService().getAllFlats();
        flatlist.enqueue(new Callback<List<FlatResponse>>() {
                             @Override
                             public void onResponse(Call<List<FlatResponse>> call, Response<List<FlatResponse>> response) {
                                 if (response.isSuccessful()) {

                                     Log.e("success", response.body().toString());
                                     for(int i=0;i<response.body().size();i++) {
                                         ModelPdf model1 = new ModelPdf( "", "","" ,"");
                                         model1.setArea(response.body().get(i).getArea());
                                         model1.setId(response.body().get(i).getId());
                                         model1.setPassword(response.body().get(i).getPassword());
                                         model1.setType(response.body().get(i).getType());

                                         pdfArrayList.add(model1);
                                         adapterPdfUser = new AdapterPdfUser(getContext(),pdfArrayList);

                                         binding.booksRv.setAdapter(adapterPdfUser);


                                     }


                                 }
                             }

                             @Override
                             public void onFailure(Call<List<FlatResponse>> call, Throwable t) {

                             }
                         });






    }

}