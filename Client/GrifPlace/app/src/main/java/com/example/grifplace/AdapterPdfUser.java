package com.example.grifplace;

import android.content.Context;
import android.content.Intent;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.Filter;
import android.widget.Filterable;
import android.widget.ImageView;
import android.widget.ProgressBar;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.example.grifplace.databinding.ActivityRowPdfUserBinding;

import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.Random;

public class AdapterPdfUser extends  RecyclerView.Adapter<com.example.grifplace.AdapterPdfUser.HolderPdfUser>  {

    private Context context;
    public ArrayList<ModelPdf> pdfArrayList;



    private ActivityRowPdfUserBinding binding;



    private  static final String TAG = "ADAPTER_PDF_USER_TFG";

    public AdapterPdfUser(Context context, ArrayList<ModelPdf> pdfArrayList) {
        this.context = context;
        this.pdfArrayList = pdfArrayList;

    }

    @NonNull
    @Override
    public HolderPdfUser onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        binding = ActivityRowPdfUserBinding.inflate(LayoutInflater.from(context),parent,false);

        return new HolderPdfUser(binding.getRoot());
    }

    @Override
    public void onBindViewHolder(@NonNull HolderPdfUser holder, int position) {
        ModelPdf model = pdfArrayList.get(position);
        final String id = model.getId();
        String area = model.getArea();
        String password = model.getPassword();
        String type = model.getType();


        holder.titleTv.setText(type);
        holder.descriptionTv.setText(area+ " м²");
        holder.categoryTv.setText("№"+id+", ");


        holder.itemView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(context,InputPasswordActivity.class) ;
                intent.putExtra("id", id);
                intent.putExtra("type", type);
                intent.putExtra("password", password);
                intent.putExtra("area", area);
                context.startActivity(intent);
            }
        });



    }

    @Override
    public int getItemCount() {
        return pdfArrayList.size();
    }


    class HolderPdfUser extends RecyclerView.ViewHolder{


        TextView titleTv, descriptionTv,categoryTv,sizeTv,dataTv,ratingTv;
        ImageView imageTv;
        Button buttonTv;
        ProgressBar progressBar;
        public HolderPdfUser(@NonNull View itemView) {
            super(itemView);


            titleTv = binding.titleTv;
            descriptionTv = binding.decriptionTv;
            categoryTv = binding.categoryTv;
            imageTv = binding.ImageFlat;
            dataTv = binding.dataTv;
            buttonTv = binding.buttonNext;
        }
    }

}

