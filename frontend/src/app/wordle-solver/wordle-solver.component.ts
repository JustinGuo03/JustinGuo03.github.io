import { Component, OnInit, ViewChildren, QueryList, ElementRef, Output, EventEmitter } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Word } from './wordle.model';
import { WordleService } from './wordle.service';
import { Observable } from 'rxjs';


@Component({
  selector: 'app-wordle-solver',
  standalone: true,
  imports: [],
  templateUrl: './wordle-solver.component.html',
  styleUrl: './wordle-solver.component.css'
})
export class WordleSolverComponent implements OnInit{
  guess: Word = {
    id: 0,
    letter1: '',
    letter2: '',
    letter3: '',
    letter4: '',
    letter5: '',
    score: 0,
    word: ''
  };

  @ViewChildren('box') boxElements!: QueryList<ElementRef>;
  @Output() colorSubmit = new EventEmitter<number[]>();

  letters = [this.guess.letter1, this.guess.letter2, this.guess.letter3, this.guess.letter4, this.guess.letter5];
  colors = ['white', 'yellow', 'green'];
  colorValues: { [key: string]: number } = {
    'white': 0,
    'yellow': 1,
    'green': 2
  };

  constructor(
    public route: Router,
    public wordleService: WordleService
  ){}
  ngOnInit(): void {
    this.wordleService.createDefaultTable(this.guess);
    this.makeGuess()
    this.updateLetters()
  }

  makeGuess(): void {
    this.wordleService
      .getWord()
      .subscribe((word) => (this.guess = word));
  }

  changeColor(box: HTMLElement): void {
    const currentColor = box.className.split(' ')[1];
    const nextColorIndex = (this.colors.indexOf(currentColor) + 1) % this.colors.length;
    box.className = `box ${this.colors[nextColorIndex]}`;
  }

  submitColors(): void {
    const colorData = this.boxElements.map(boxRef => {
      const box = boxRef.nativeElement;
      const color = box.className.split(' ')[1];
      return this.colorValues[color];
    });
    console.log('Color data:', colorData);
    this.colorSubmit.emit(colorData);
  }

  updateLetters(): void {
    this.letters = [this.guess.letter1, this.guess.letter2, this.guess.letter3, this.guess.letter4, this.guess.letter5];
  }
}
