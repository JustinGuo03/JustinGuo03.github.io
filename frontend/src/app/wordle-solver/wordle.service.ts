import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { Observable, ReplaySubject } from 'rxjs';
import { Word } from './wordle.model';

@Injectable({
  providedIn: 'root'
})
export class WordleService {
//   private words: ReplaySubject<Word[]> = new ReplaySubject(1);
//   guess$: Observable<Word[]> = this.words.asObservable();

//   private wordLetters: ReplaySubject<Word[]> =
//     new ReplaySubject(1);
//   articleHeadlines$: Observable<Word[]> =
//     this.articleHeadlines.asObservable();

  // TODO: implement other methods and constructor
  constructor(
    protected http: HttpClient
  ) {
  }

  /** Returns all articles entries from the backend database table using the backend HTTP get request.
//    * @returns {Observable<Word[]>}
//    */
//   getWords() {
//     this.http
//       .get<Word[]>('/api/wordle')
//       .subscribe((word) => this.words.next(word));
//   }


  /** Returns the article object from the backend database table using the backend HTTP get request.
   * @param slug: String representing the article slug
   * @returns {Observable<Word>}
   */
  getWord(): Observable<Word> {
    return this.http.get<Word>('/api/wordle/');
  }

  /** Returns the new article object from the backend database table using the backend HTTP post request.
   * @param article: AdrticleSummary representing the new article
   * @returns {Observable<Organization>}
   */
  createWord(request: Word): Observable<Word> {
    return this.http.post<Word>('/api/wordle', request);
  }

  deleteWord(slug: Word) {
    return this.http.delete('/api/wordle/' + slug);
  }

  createDefaultTable(request: Word) {
    return this.http.post<Word[]>('/api/wordle/', request);
  }
}
