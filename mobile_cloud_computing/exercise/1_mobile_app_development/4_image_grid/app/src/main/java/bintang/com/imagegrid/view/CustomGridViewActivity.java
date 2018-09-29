package bintang.com.imagegrid.view;

import android.content.Context;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.TextView;

import com.squareup.picasso.Picasso;

import java.util.List;

import bintang.com.imagegrid.R;

public class CustomGridViewActivity extends BaseAdapter {
    private LayoutInflater inflater;
    private Context mContext;
    private List<String> authorsName;
    private List<String> imageUrls;

    public CustomGridViewActivity(Context context, List<String> authorsNames, List<String> imageUrls) {
        mContext = context;
        inflater = (LayoutInflater.from(context));
        this.authorsName = authorsNames;
        this.imageUrls = imageUrls;
    }

    @Override
    public int getCount() {
        return this.authorsName.size();
    }

    @Override
    public Object getItem(int position) {
        return null;
    }

    @Override
    public long getItemId(int position) {
        return 0;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        View gridViewNew;
        inflater = (LayoutInflater) mContext
                .getSystemService(Context.LAYOUT_INFLATER_SERVICE);

        gridViewNew = new View(mContext);

        gridViewNew = inflater.inflate(R.layout.image_text_layout, null); // inflate the layout
        ImageView theImage = (ImageView) gridViewNew.findViewById(R.id.theImageInGrid);
        TextView authorsNameView = (TextView) gridViewNew.findViewById(R.id.authorsText);

        authorsNameView.setText(this.authorsName.get(position));
        Picasso.get().load(this.imageUrls.get(position)).into(theImage);
        return gridViewNew;
    }
}
