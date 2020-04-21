import { Component, OnInit } from '@angular/core';
import { Tweet } from '../tweet.model';

@Component({
  selector: 'app-tweet',
  templateUrl: './tweet.component.html',
  styleUrls: ['./tweet.component.css']
})
export class TweetComponent implements OnInit {

  tweet = new Tweet(
    './../../../assets/img/donald-trump.jpg',
    'Donald J. Trump',
    'realDonaldTrump',
    'Just Now',
    'I am officially stepping down as President of the United States!',
    false
  );

  constructor() { }

  ngOnInit(): void {
  }

}
