package bintang.com.imagegrid;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.GridView;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

import bintang.com.imagegrid.data.model.JsonDataModel;
import bintang.com.imagegrid.data.remote.ApiUtils;
import bintang.com.imagegrid.data.remote.JsonAccessService;
import bintang.com.imagegrid.view.CustomGridViewActivity;
import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.annotations.NonNull;
import io.reactivex.observers.DisposableObserver;
import io.reactivex.schedulers.Schedulers;

public class MainActivity extends AppCompatActivity {
    private JsonAccessService jsonAccessService;
    private GridView theGridView;
    private static final String TAG = "MCC";

    private enum SortingMode {
        ASCENDING, DESCENDING, DATE
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button buttonAsc = (Button) findViewById(R.id.sortAsc);
        Button buttonDesc = (Button) findViewById(R.id.sortDes);
        Button buttonDate = (Button) findViewById(R.id.sortDate);

        buttonAsc.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                getJsonFile(SortingMode.ASCENDING);
            }
        });

        buttonDesc.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                getJsonFile(SortingMode.DESCENDING);
            }
        });

        buttonDate.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                getJsonFile(SortingMode.DATE);
            }
        });

    }

    private void displayImage(List<String> authors, List<String> urls) {
        theGridView = (GridView) findViewById(R.id.theGridLayout);
        CustomGridViewActivity customGridAdapter =
                new CustomGridViewActivity(getApplicationContext(), authors, urls);

        theGridView.setAdapter(customGridAdapter);
    }

    private void getJsonFile(final SortingMode sortingMode) {
        EditText inputUrl = (EditText) findViewById(R.id.txtUrl);
        String theUrl = inputUrl.getText().toString();

        jsonAccessService = ApiUtils.getJsonAccessService();

        jsonAccessService.getJsonFile(theUrl)
                .subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread())
                .subscribe(new DisposableObserver<List<JsonDataModel>>() {
                    @Override
                    public void onNext(@NonNull List<JsonDataModel> jsonDataModel) {

                        switch (sortingMode) {
                            case ASCENDING:
                                jsonDataModel.sort(Comparator.comparing(JsonDataModel::getAuthor));
                                break;
                            case DESCENDING:
                                jsonDataModel.sort(Comparator.comparing(JsonDataModel::getAuthor).reversed());
                                break;
                            case DATE:
                                jsonDataModel.sort(Comparator.comparing(JsonDataModel::getDate).reversed());
                                break;
                        }

                        List<String> authorsList = new ArrayList<String>();
                        List<String> imageUrlList = new ArrayList<String>();

                        for(JsonDataModel element : jsonDataModel) {
                            Log.d(TAG, "author: " + element.getAuthor() + ", date: " + element.getDate());
                            authorsList.add(element.getAuthor());
                            imageUrlList.add(element.getPhoto());
                        }
                        displayImage(authorsList, imageUrlList);
                    }

                    @Override
                    public void onError(@NonNull Throwable e) {
                        Log.e(TAG, "error: " + e.getMessage());
                    }

                    @Override
                    public void onComplete() {
                        Log.d(TAG, "Complete");
                    }
                });
    }
}
