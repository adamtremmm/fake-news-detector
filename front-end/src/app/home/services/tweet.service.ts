import { Injectable } from '@angular/core';
import { Tweet } from '../models/tweet.model';
import { Subject } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Injectable({providedIn: 'root'})
export class TweetService {
  private tweets: Tweet[] = [];
  private tweetsUpdated = new Subject<Tweet[]>();

  constructor(
    private http: HttpClient
  ) {}

  postTweet(tweet: Tweet) {
    this.http.post<{ prediction: string }>('http://localhost:5000/fakenews/api/v1.0/predict', { tweet: tweet.text })
      .subscribe((response) => {
        tweet.isTrue = response.prediction;
        this.tweets.unshift(tweet);
        this.tweetsUpdated.next([...this.tweets]);
      });
  }

  getTweets() {
    return [...this.tweets];
  }

  getTweetUpdateListener() {
    return this.tweetsUpdated.asObservable();
  }
}
